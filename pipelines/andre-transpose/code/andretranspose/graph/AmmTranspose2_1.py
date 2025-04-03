from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def AmmTranspose2_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import pyspark.sql.functions as F
    #print(">> Hello Transpose")
    print(">> key_columns.0:", [])
    print(">> value_columns.0:", [])
    key_columns = ["products"]
    print(">> key_columns.1:", ["products"])
    print(">> value_columns.1:", ["small", "medium", "large"])
    name_column = "value"
    df = in0
    print(">> Hello Transpose")
    # NOTE: optimizer doesn't yet support list comprehension
    available_data_columns = []

    if "small" in in0.columns:
        available_data_columns = ["small"]

    if "medium" in in0.columns:
        available_data_columns.append("medium")

    if "large" in in0.columns:
        available_data_columns.append("large")

    dfs = []

    for data_col_name in available_data_columns:
        selected_df = df.select(
            (
              [F.col(key_col) for key_col in key_columns]
              + [F.lit(data_col_name).cast("string").alias(name_column),
                                 F.col(data_col_name).cast("string").alias(name_column)]
            )
        )
        dfs.append(selected_df)

    transposed_df = dfs[0]

    for other_df in dfs[1:]:
        transposed_df = transposed_df.union(other_df)

    print(">> END")

    #print(">> transposed_df:", transposed_df.count())
    return transposed_df
