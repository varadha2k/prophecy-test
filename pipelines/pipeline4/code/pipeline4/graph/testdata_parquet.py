from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline4.config.ConfigStore import *
from pipeline4.functions import *

def testdata_parquet(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("s3://bh-d-airflow-testing/output/")
