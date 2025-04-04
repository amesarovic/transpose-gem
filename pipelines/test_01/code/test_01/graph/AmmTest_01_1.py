from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_01.config.ConfigStore import *
from test_01.functions import *

def AmmTest_01_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print(">> apply")
    df1 = in0.select(*[col for col in in0.columns if col != "products"])

    return df1.limit(5)
