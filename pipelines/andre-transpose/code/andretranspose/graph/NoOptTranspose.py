from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def NoOptTranspose(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from typing import Optional, List, Dict
    from dataclasses import dataclass, field
    from abc import ABC
    
    from pyspark.sql.column import Column
    from pyspark.sql.functions import col
    from dataclasses import dataclass
    from typing import Optional, List, Dict
    from pyspark.sql.column import Column as sparkColumn


    @dataclass(frozen = True)
    class SColumn:
        expression: Optional[Column] = None

        @staticmethod
        def getSColumn(column: str):
            return SColumn(col(column))

        def column(self) -> sparkColumn:
            return self.expression

        def columnName(self) -> str:
            return self.expression._jc.toString()


    @dataclass(frozen = True)
    class SColumnExpression:
        target: str
        expression: SColumn
        description: str
        _row_id: Optional[str] = None

        @staticmethod
        def remove_backticks(s):
            if s.startswith("`") and s.endswith("`"):
                return s[1:- 1]
            else:
                return s

        @staticmethod
        def getColumnExpression(column: str):
            return SColumnExpression(column, SColumn.getSColumn(col(column)), "")

        @staticmethod
        def getColumnsFromColumnExpressionList(columnExpressions: list):
            columnList = []

            for expression in columnExpressions:
                columnList.append(expression.expression)

            return columnList

        def column(self) -> Column:

            if (self.expression.columnName() == SColumnExpression.remove_backticks(self.target)):
                return self.expression.expression

            return self.expression.expression.alias(self.target)


    @dataclass(frozen = True)
    class AmmTransposeNoOptProperties():
        pivot_column: str = str("pivot column")
        key_columns: list[str] = field(default_factory = list)
        value_columns: list[str] = field(default_factory = list)

    props = AmmTransposeNoOptProperties(  #skiptraversal
        pivot_column = "pivot column", 
        key_columns = ["products"], 
        value_columns = ["small", "medium", "large"]
    )
    in0 = in0
    import pyspark.sql.functions as F
    data_columns = [col_name for col_name in props.value_columns if col_name in in0.columns]
    dfs = [
              in0.select(
                (
                  [F.col(key_col) for key_col in props.key_columns]
                  + [F.lit(data_col_name).cast("string").alias("Name"),
                                         F.col(data_col_name).cast("string").alias("Value")]
                )
              )
              for data_col_name in data_columns
              ]
    transposed_df = dfs[0]

    for df in dfs[1:]:
        transposed_df = transposed_df.union(df)

    return transposed_df
