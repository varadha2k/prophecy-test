from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline4.config.ConfigStore import *
from pipeline4.functions import *

def filter_by_age(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("age") > lit(20)))
