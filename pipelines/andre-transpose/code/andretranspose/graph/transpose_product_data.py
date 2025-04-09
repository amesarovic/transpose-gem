from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *

def transpose_product_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import pyspark.sql.functions as F

    #return dfs[0]
    return in0
