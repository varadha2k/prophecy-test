from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *

def filter_by_c3_value(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("_c3") == lit("14")))
