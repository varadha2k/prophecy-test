from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *

def testdata1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("MALLA REDDY INSTITTUTE OF MANAGEMENT", StringType(), True), StructField("_c1", StringType(), True), StructField("_c2", StringType(), True), StructField("_c3", StringType(), True), StructField("_c4", StringType(), True), StructField("_c5", StringType(), True), StructField("_c6", StringType(), True), StructField("_c7", StringType(), True), StructField("_c8", StringType(), True), StructField("_c9", StringType(), True), StructField("_c10", StringType(), True), StructField("_c11", StringType(), True), StructField("col2    ", IntegerType(), False)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("s3://bh-d-airflow-testing/data/mc student list updated.csv")
