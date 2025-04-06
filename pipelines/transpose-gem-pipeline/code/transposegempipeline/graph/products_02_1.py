from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from transposegempipeline.config.ConfigStore import *
from transposegempipeline.functions import *

def products_02_1(spark: SparkSession) -> DataFrame:
    return spark.read.option("header", True).option("sep", ",").csv("dbfs:/user/andre/data/products/products_02.csv")
