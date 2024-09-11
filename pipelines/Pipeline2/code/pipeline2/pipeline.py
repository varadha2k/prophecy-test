from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline2.config.ConfigStore import *
from pipeline2.functions import *
from prophecy.utils import *
from pipeline2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_testdata1 = testdata1(spark)
    df_Filter_1 = Filter_1(spark, df_testdata1)
    testdata_parquet(spark, df_Filter_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pipeline2")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline2")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Pipeline2", config = Config)(pipeline)

if __name__ == "__main__":
    main()
