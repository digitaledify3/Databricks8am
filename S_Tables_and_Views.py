# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
# MAGIC %md
# MAGIC Tables And Views

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace schema training8am1

# COMMAND ----------

# MAGIC %sql
# MAGIC use training8am1

# COMMAND ----------

# MAGIC %sql
# MAGIC create table employees(id int , name string, dept string, salary decimal(8,5) , joiningdate date ,active boolean);

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE employees SET TBLPROPERTIES ('delta.columnMapping.mode' = 'name');
# MAGIC ALTER TABLE employees DROP COLUMN salary_new;
# MAGIC ALTER TABLE employees ADD COLUMN salary_new DECIMAL(10,2);
# MAGIC UPDATE employees SET salary_new = salary;
# MAGIC ALTER TABLE employees DROP COLUMN salary;
# MAGIC ALTER TABLE employees RENAME COLUMN salary_new TO salary;

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into employees values
# MAGIC (1,'John','Sales','2019-01-01',true,100000.00),
# MAGIC (2,'Mary','Sales','2019-01-01',true,120000.00),
# MAGIC (3,'Mike','IT','2019-01-01',true,150000.00),
# MAGIC (4,'Sue','IT','2019-01-01',true,180000.00),
# MAGIC (5,'Pete','HR','2019-01-01',true,120000.00),
# MAGIC (6,'Paul','HR','2019-01-01',true,150000.00),
# MAGIC (7,'Sally','Sales','2019-01-01',false,100000.00),
# MAGIC (8,'Jane','Sales','2019-01-01',false,120000.00),
# MAGIC (9,'Bob','IT','2019-01-01',false,150000.00),
# MAGIC (10,'Sara','IT','2019-01-01',false,180000.00),
# MAGIC (11,'Tom','HR','2019-01-01',false,120000.00)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees

# COMMAND ----------

# MAGIC %sql
# MAGIC describe employees

# COMMAND ----------

# MAGIC %sql
# MAGIC create view if not exists employees_view as select * from employees

# COMMAND ----------

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ServicesData").getOrCreate()

# Define the data
data = [
    ("S001", "P101", "C567", "COMPLETED", 2500, "2026-06-20"),
    ("S002", "P102", "C568", "PENDING", 1800, "2026-06-21"),
    ("S003", "P103", "C569", "INPROGRESS", 3200, "2026-06-22"),
    ("S004", "P104", "C570", "CANCELLED", 0, "2026-06-23"),
]

# Define the schema (column names)
columns = ["ServiceID", "ProductID", "CustomerID", "Status", "ServiceCharges", "ServiceRequestDate"]

# Create the DataFrame
servicesdf = spark.createDataFrame(data, columns)

# Show the DataFrame
servicesdf.show()

# COMMAND ----------

from pyspark.sql.functions import col
statusinprocesdf=servicesdf.filter(col("status")=="INPROGRESS")
display(statusinprocesdf)

# COMMAND ----------

from pyspark.sql.functions import col
completeddf=servicesdf.filter(col("status")=="COMPLETED")
display(completeddf)

# COMMAND ----------

# MAGIC %md
# MAGIC completeddf.saveAsTable("ServicesCompleted")
# MAGIC statusinprocesdf.saveAsTable("ServisesInProces")
# MAGIC
# MAGIC CREATE TABLE ServicesCompleted AS SELECT * FROM completeddf;
# MAGIC CREATE TABLE ServisesInProces AS SELECT * FROM statusinprocesdf;

# COMMAND ----------



completeddf.write.mode("overwrite").saveAsTable("training8am1.ServicesCompleted")
statusinprocesdf.write.mode("overwrite").saveAsTable("training8am1.ServisesInProces")
servicesdf.write.mode("overwrite").saveAsTable("training8am1.Services")

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table ServicesCompleted;
# MAGIC drop table ServisesInProces;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from training8am1.ServicesCompleted

# COMMAND ----------

# MAGIC %sql
# MAGIC create view if not exists training8am1.ServicesCompletedView as select * from training8am1.ServicesCompleted

# COMMAND ----------

# MAGIC %sql
# MAGIC create view if not exists training8am1.servisesinprocesView as select * from training8am1.ServisesInProces
# MAGIC

# COMMAND ----------

servicesdf.show()

# COMMAND ----------

servicesdf.createOrReplaceTempView("servicesview")

# COMMAND ----------

spark.sql("select * from servicesview where status='COMPLETED").show();

# COMMAND ----------

# MAGIC %md
# MAGIC to drop the column or table we need to specify the delta table by setting some properties 
# MAGIC column mapping mode , it is okay to restructure table
# MAGIC
