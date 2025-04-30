# Databricks notebook source
# MAGIC %md
# MAGIC ##**Data Accessing**

# COMMAND ----------

dbutils.fs.ls("abfss://bronzelayer@nyctaxistorage29.dfs.core.windows.net")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Data Reading##

# COMMAND ----------

# MAGIC %md
# MAGIC  **Importing Libaries**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC Reading CSV

# COMMAND ----------

df_trip_type = spark.read.format("csv")\
                .option("inferscehma",True)\
                .option("header",True)\
                .load('abfss://bronzelayer@nyctaxistorage29.dfs.core.windows.net/trip_type')
df_trip_type = df_trip_type.withColumn('trip_type',df_trip_type['trip_type'].cast('int'))
df_trip_type = df_trip_type.withColumnRenamed('description','Trip_description')
display(df_trip_type)


# COMMAND ----------

df_trip_zone = spark.read.format("csv")\
                .option("inferscehma",True)\
                .option("header",True)\
                .load('abfss://bronzelayer@nyctaxistorage29.dfs.core.windows.net/tirp_zone')
df_trip_zone = df_trip_zone.withColumn('Locationid', df_trip_zone['Locationid'].cast('int'))
display(df_trip_zone)

# COMMAND ----------

myschema = '''
VendorID BIGINT,
lpep_pickup_datetime TIMESTAMP,
lpep_dropoff_datetime TIMESTAMP,
store_and_fwd_flag STRING,
RatecodeID BIGINT,
PULocationID BIGINT,
DOLocationID BIGINT,
passenger_count BIGINT,
trip_distance DOUBLE,
fare_amount DOUBLE,
extra DOUBLE,
mta_tax DOUBLE,
tip_amount DOUBLE,
tolls_amount DOUBLE,
ehail_fee DOUBLE,
improvement_surcharge DOUBLE,
total_amount DOUBLE,
payment_type BIGINT,
trip_type BIGINT,
congestion_surcharge DOUBLE
'''

# COMMAND ----------

df_trip = spark.read.format("parquet")\
                .option("myschema",True)\
                .option("header",True)\
                .option("recursivefilelookup","true")\
               .load('abfss://bronzelayer@nyctaxistorage29.dfs.core.windows.net/Triprawdata2024')
display(df_trip)

# COMMAND ----------

# MAGIC %md
# MAGIC # **Data Transformation**

# COMMAND ----------

# MAGIC %md
# MAGIC Write data to silver layer after transformation done previous, while reading data

# COMMAND ----------

df_trip_type.write.format('parquet')\
    .mode('append')\
    .option('path','abfss://silverlayer@nyctaxistorage29.dfs.core.windows.net/Trip_type')\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC Spliitng columns with split function

# COMMAND ----------

df_trip_zone = df_trip_zone.withColumn('zone-1',split('zone','/')[0])\
                            .withColumn('zone-2',split('zone','/')[1])
df_trip_zone.display()

# COMMAND ----------

df_trip_zone.write.format('parquet')\
    .mode('append')\
    .option('path','abfss://silverlayer@nyctaxistorage29.dfs.core.windows.net/Trip_zone')\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC Spliting column based on date and month and year with help of split function and inbuilt datefunction

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_trip = df_trip.withColumn('pickup_datetime',to_date('lpep_pickup_datetime',format='DD/MM/yyyy'))\
                .withColumn('pickup_month',month('lpep_pickup_datetime'))\
                .withColumn('pickup_Year',year('lpep_pickup_datetime'))

# COMMAND ----------

df_trip.display()

# COMMAND ----------

df_tirp_gold_layer=df_trip.select('vendorid','PULocationID','DOLocationID','trip_distance','fare_amount','total_amount')

# COMMAND ----------

df_tirp_gold_layer.display()

# COMMAND ----------

df_tirp_gold_layer.write.format('parquet')\
    .mode('append')\
    .option('path','abfss://silverlayer@nyctaxistorage29.dfs.core.windows.net/Trip_2024_data')\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Analysis**

# COMMAND ----------

display(df_tirp_gold_layer)


# COMMAND ----------

