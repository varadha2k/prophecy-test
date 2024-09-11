from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline2.config.ConfigStore import *
from pipeline2.functions import *

def testdata_parquet(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").save("s3://bh-d-airflow-testing/output/")
