# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SampleData").getOrCreate()

data = [
    (1, "Rahul", 25, "Hyderabad", 35000),
    (2, "Priya", 30, "Bangalore", 50000),
    (3, "Amit", 28, "Mumbai", 45000),
    (4, "Sneha", 35, "Chennai", 60000),
    (5, "Kiran", 22, "Hyderabad", 30000)
]

columns = ["ID", "Name", "Age", "City", "Salary"]

df = spark.createDataFrame(data, columns)

df.show()

# COMMAND ----------

from pyspark.sql.functions import col
df.filter(col("City")=="Hyderabad").show()
