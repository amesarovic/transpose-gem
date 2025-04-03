from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def AmmTranspose2_1(spark: SparkSession, in0: DataFrame) -> DataFrame:

    def bar(df):
        return df.limit(10)

    print(">> key_columns.1:", [])
    print(">> key_columns.2:", ["products"])

    #return in0
    #return in0.limit(10)
    return bar(in0)
