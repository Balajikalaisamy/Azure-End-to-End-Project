# Databricks notebook source
# MAGIC %md
# MAGIC Data Access 

# COMMAND ----------

# COMMAND ----------

# MAGIC %md
# MAGIC Data Base creation 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists trip_zone; 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC drop database if exists gold cascade;
# MAGIC create database gold;
# MAGIC use database gold

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Reading,Data writing and creating delta tables

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC  **Importing Libaries**

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC DATA Zone 

# COMMAND ----------

#Storage Variable 
Silver = "abfss://silverlayer@nyctaxistorage29.dfs.core.windows.net"
Gold = "abfss://goldlayer@nyctaxistorage29.dfs.core.windows.net"

# COMMAND ----------

df_zone = spark.read.format("parquet")\
                    .option("header", "true")\
                    .option("inferSchema", "true")\
                    .load(f'{Silver}/Trip_zone')
df_zone.display()


# COMMAND ----------

# MAGIC %md
# MAGIC Data Writing on Gold layer in delta table

# COMMAND ----------

# MAGIC %md
# MAGIC **Loading zone data in form of delta format**

# COMMAND ----------

df_zone.write.format("delta")\
    .mode('append')\
    .option('path', 'abfss://goldlayer@nyctaxistorage29.dfs.core.windows.net/Trip_zone')\
    .saveAsTable('gold.trip_zone')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_zone;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Loading  Trip _type data in form of delta format**

# COMMAND ----------

df_trip_type  = spark.read.format("parquet")\
                    .option("header", "true")\
                    .option("inferSchema", "true")\
                    .load(f'{Silver}/Trip_type')
df_type.display()

# COMMAND ----------

df_trip_type.write.format("delta")\
    .mode('append')\
    .option('path', 'abfss://goldlayer@nyctaxistorage29.dfs.core.windows.net/trip_type')\
    .saveAsTable('gold.trip_type')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_type;

# COMMAND ----------

# MAGIC %md
# MAGIC **Loading  Trip_data_2024 data in form of delta format**

# COMMAND ----------

df_trip_data  = spark.read.format("parquet")\
                    .option("header", "true")\
                    .option("inferSchema", "true")\
                    .load(f'{Silver}/Trip_2024_data')
df_trip_data.display()

# COMMAND ----------

df_trip_data.write.format("delta")\
    .mode('append')\
    .option('path', 'abfss://goldlayer@nyctaxistorage29.dfs.core.windows.net/trip_data')\
    .saveAsTable('gold.trip_data')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_data;

# COMMAND ----------

# MAGIC %md
# MAGIC Learning Delta Lake Versioning 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_zone;

# COMMAND ----------

# MAGIC %sql
# MAGIC update trip_zone set Borough = 'RWE' where Locationid=1;
# MAGIC select * from trip_zone;

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from trip_zone where Locationid=1;
# MAGIC select * from trip_zone;

# COMMAND ----------

# MAGIC %md
# MAGIC Versioning delta lake sample 

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history trip_zone

# COMMAND ----------

# MAGIC %md
# MAGIC *Restoring version from delta log*

# COMMAND ----------

# MAGIC %sql
# MAGIC restore trip_zone VERSION AS OF 1;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_zone;

# COMMAND ----------

# MAGIC %sql
# MAGIC restore trip_zone VERSION AS OF 0;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from trip_zone;