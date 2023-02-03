# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +

def is_notebook():
    try:
        get_ipython()
        return True
    except NameError:
        return False

if is_notebook():
    import findspark
    findspark.init('/lib/spark')
    
    import pyspark

    spark = pyspark.sql.SparkSession \
        .builder \
        .config("spark.submit.deployMode", "client") \
        .config("spark.master", "local[*]") \
        .appName("default") \
        .enableHiveSupport() \
        .getOrCreate()
else:
    import pyspark
    spark = pyspark.sql.SparkSession.builder.getOrCreate()
# -

from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType([
    StructField("product_name",StringType()),
    StructField("release_date",TimestampType()),
    StructField("version",StringType()),
    StructField("link",StringType()),
    StructField("body",StringType()),
])
df = spark.read.schema(schema).json("/lake/red/release-note")

# + jupyter={"outputs_hidden": true} tags=[]
df.write.mode("overwrite").option('compression', 'snappy').parquet('/lake/yellow/release-note')
# -


