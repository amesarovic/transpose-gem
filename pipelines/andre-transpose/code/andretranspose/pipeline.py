from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from andretranspose.config.ConfigStore import *
from andretranspose.functions import *
from prophecy.utils import *
from andretranspose.graph import *

def pipeline(spark: SparkSession) -> None:
    df_products_02_1 = products_02_1(spark)
    df_transpose_product_data = transpose_product_data(spark, df_products_02_1)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("andre-transpose").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/andre-transpose")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/andre-transpose", config = Config)(pipeline)

if __name__ == "__main__":
    main()
