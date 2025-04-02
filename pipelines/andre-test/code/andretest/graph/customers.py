from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretest.config.ConfigStore import *
from andretest.functions import *

def customers(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("_c0", StringType(), True), StructField("crim", StringType(), True), StructField("zn", StringType(), True), StructField("indus", StringType(), True), StructField("chas", StringType(), True), StructField("nox", StringType(), True), StructField("rm", StringType(), True), StructField("age", StringType(), True), StructField("dis", StringType(), True), StructField("rad", StringType(), True), StructField("tax", StringType(), True), StructField("ptratio", StringType(), True), StructField("black", StringType(), True), StructField("lstat", StringType(), True), StructField("medv", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/Boston.csv")
