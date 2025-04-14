from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sqlgemtest.config.ConfigStore import *
from sqlgemtest.functions import *
from prophecy.utils import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("sql-gem-test").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/sql-gem-test")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/sql-gem-test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
