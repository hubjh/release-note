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
        .config("spark.ui.enabled", "false") \
        .appName("default") \
        .enableHiveSupport() \
        .getOrCreate()
else:
    import pyspark
    spark = pyspark.sql.SparkSession.builder.getOrCreate()
# -

df = spark.read.parquet('/lake/yellow/release-note')
df.createOrReplaceTempView("release_note")

df = spark.sql("SELECT product_name, version, link, release_date FROM release_note ORDER BY release_date DESC")

df.show()

data = []
for row in df.collect():
    row = list(row)
    row[3] = row[3].isoformat()
    data.append(list(row))

import requests
response = requests.post('http://15.164.106.168/api/v1/update', json=data)
print(response.text)
response.raise_for_status()

# +
# s3_client.get_objects()
# cursor = conn.cursor()
# cursor.execute(
#     'SELECT product_name, version, link, release_date FROM y_release_note.release_note ORDER BY release_date DESC')
# data = cursor.fetchall()
