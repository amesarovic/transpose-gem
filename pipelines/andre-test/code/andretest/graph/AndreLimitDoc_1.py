from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretest.config.ConfigStore import *
from andretest.functions import *

def AndreLimitDoc_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    # This method contains logic used to generate the spark code from the given inputs.
    return in0
