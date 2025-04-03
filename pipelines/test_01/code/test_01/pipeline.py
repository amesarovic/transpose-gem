from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_01.config.ConfigStore import *
from test_01.functions import *
from prophecy.utils import *
from test_01.graph import *

def pipeline(spark: SparkSession) -> None:
    df_products_50_1 = products_50_1(spark)
    df_limit_to_20 = limit_to_20(spark, df_products_50_1)
    df_products_50_1_1 = products_50_1_1(spark)
    df_products_50_1_1_1 = products_50_1_1_1(spark)
    df_products_50 = products_50(spark)
    df_AndreTest_1 = AndreTest_1(spark, df_products_50)
    df_AmmLimitNoop = AmmLimitNoop(spark, df_products_50_1_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("test_01").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_01")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test_01", config = Config)(pipeline)

if __name__ == "__main__":
    main()
