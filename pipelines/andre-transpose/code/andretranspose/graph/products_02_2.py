from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def products_02_2(spark: SparkSession) -> DataFrame:
    return spark.read.option("header", True).option("sep", ",").csv("dbfs:/user/andre/data/products/products_02.csv")
