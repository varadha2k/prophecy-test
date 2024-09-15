from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline4.config.ConfigStore import *
from pipeline4.functions import *
from prophecy.utils import *
from pipeline4.graph import *

def pipeline(spark: SparkSession) -> None:
    df_testdata_parquet = testdata_parquet(spark)
    df_add_constant_column = add_constant_column(spark)
    testdata1(spark, df_add_constant_column)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipeline4")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline4")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline4", config = Config)(pipeline)

if __name__ == "__main__":
    main()
