from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def NewTranspose(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import pyspark.sql.functions as F
    available_data_columns = []

    if "small" in in0.columns:
        available_data_columns = ["small"]

    if "medium" in in0.columns:
        available_data_columns.append("medium")

    if "large" in in0.columns:
        available_data_columns.append("large")

    dfs = []
    keyColumns: SubstitueDisabled = ["products"]

    for data_col_name in available_data_columns:
        selection: SubstitueDisabled = []

        for key_col in keyColumns:
            selection.append(col(key_col))

        selection.append(lit(data_col_name).cast("string").alias("Name"))
        selection.append(col(data_col_name).cast("string").alias("Value"))
        df_selected: SubstitueDisabled = in0.select(*selection)
        dfs.append(df_selected)

    transposed_df = dfs[0]

    for other_df in dfs[1:]:
        transposed_df = transposed_df.union(other_df)

    return transposed_df
