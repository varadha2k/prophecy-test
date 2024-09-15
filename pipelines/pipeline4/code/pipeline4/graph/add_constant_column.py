from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline4.config.ConfigStore import *
from pipeline4.functions import *

def add_constant_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("col2    ", lit(10))
