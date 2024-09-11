from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *
from prophecy.utils import *
from pipeline1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_testdata1 = testdata1(spark)
    df_name_filter = name_filter(spark)
    df_Deduplicate_1 = Deduplicate_1(spark, df_name_filter)
    df_SchemaTransform_1 = SchemaTransform_1(spark)
    df_filter_by_c3_value = filter_by_c3_value(spark, df_testdata1)
    testdata_parquet(spark, df_filter_by_c3_value)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipeline1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
