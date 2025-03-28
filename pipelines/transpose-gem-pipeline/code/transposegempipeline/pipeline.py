from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from transposegempipeline.config.ConfigStore import *
from transposegempipeline.functions import *
from prophecy.utils import *
from transposegempipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("transpose-gem-pipeline").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/transpose-gem-pipeline")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/transpose-gem-pipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
