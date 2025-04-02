from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from andretest.config.ConfigStore import *
from andretest.functions import *
from prophecy.utils import *
from andretest.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_concat_zn_indus = concat_zn_indus(spark, df_customers)
    df_SampleRows_1 = SampleRows_1(spark)
    df_limit_to_50 = limit_to_50(spark)
    df_AndreLimitDoc_1 = AndreLimitDoc_1(spark, df_limit_to_50)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("andre-test").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/andre-test")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/andre-test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
