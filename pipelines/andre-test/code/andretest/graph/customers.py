from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretest.config.ConfigStore import *
from andretest.functions import *

def customers(spark: SparkSession) -> DataFrame:
    return spark.read.option("header", True).option("sep", ",").csv("dbfs:/FileStore/Boston.csv")
