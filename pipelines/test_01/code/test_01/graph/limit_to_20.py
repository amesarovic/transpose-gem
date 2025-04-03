from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_01.config.ConfigStore import *
from test_01.functions import *

def limit_to_20(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(20)
