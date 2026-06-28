# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
# MAGIC %sql
# MAGIC select * from training8am1.services

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM training8am1.SERVICES WHERE Status = 'COMPLETED';

# COMMAND ----------

# MAGIC %sql
# MAGIC create procedure if not exists GetCompletedServices()
# MAGIC SQL SECURITY invoker
# MAGIC LANGUAGE SQL 
# MAGIC AS 
# MAGIC BEGIN
# MAGIC     SELECT * FROM training8am1.SERVICES WHERE Status = 'COMPLETED';
# MAGIC END;

# COMMAND ----------

# MAGIC %sql
# MAGIC CALL GetCompletedServices();
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create procedure if not exists customerservicehistory()
# MAGIC sql query inovker
# MAGIC language sql
# MAGIC as 
# MAGIC begin
# MAGIC     select customerName,
# MAGIC     ServiceId,
# MAGIC     status,
# MAGIC     ServiceCharges
# MAGIC     from training8am1.customerview c
# MAGIC     left join training8am1.services s
# MAGIC     on c.CustomerId = s.CustomerId;
# MAGIC end
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC call customerservicehistory();

# COMMAND ----------

# MAGIC %md
# MAGIC **create store procesdures for all these**
# MAGIC - Area wise Revenue
# MAGIC - get product table : vendore revenue
# MAGIC - productwise service count
# MAGIC - get all the services who has a charge greater than the charge given as input and status given as input
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #parametrised store procedures

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE PROCEDURE IF NOT EXISTS TRAINING8AM1.INPUTFROMCUSTOMER(ID STRING)
# MAGIC SQL SECURITY INVOKER 
# MAGIC LANGUAGE SQL
# MAGIC AS 
# MAGIC BEGIN
# MAGIC     SELECT * FROM training8am1.services WHERE CustomerId = ID;
# MAGIC END;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM training8am1.services;

# COMMAND ----------

# MAGIC %sql
# MAGIC CALL TRAINING8AM1.INPUTFROMCUSTOMER("C567");
