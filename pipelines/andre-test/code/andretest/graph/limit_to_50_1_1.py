from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretest.config.ConfigStore import *
from andretest.functions import *

def limit_to_50_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(50)
