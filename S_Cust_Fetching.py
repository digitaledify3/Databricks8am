# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CustomerFetching").getOrCreate()

data = [
    ("C101", "Usha", "Tarnaka", "Occasional"),
    ("C102", "Rama", "Ameerpet", "Premium"),
    ("C103", "Deep", "Begumpet", "Regular"),
    ("C104", "Bryan", "Begumpet", "Regular"),
    ("C105", "Vijay", "Tarnaka", "Occasional"),
    ("C106", "Lalita", "Ameerpet", "Regular"),
    ("C107", "Ruhi", "Jolarpet", "Premium")
]

columns = ["CustomerId", "CustomerName", "Area", "CustomerType"]

customerdf = spark.createDataFrame(data, columns)

customerdf.show()

# COMMAND ----------

customerdf.write.mode("overwrite").saveAsTable("training8am1.customer")


# COMMAND ----------

# MAGIC %sql
# MAGIC create view if not exists training8am1.customerview as select * from training8am1.customer

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from training8am1.customerview
