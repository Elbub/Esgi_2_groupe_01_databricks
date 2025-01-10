# Databricks notebook source
SCOPE = "Esgi_2_groupe_01_scope"
STORAGE_ACCOUNT_NAME = "esgi2groupe01storage"
CONTAINER_NAME = "esgi-2-groupe-01-container"
STORAGE_ACCOUNT_KEY = "Esgi-2-groupe-01-storage-key-secret"

# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://" + CONTAINER_NAME + "@" + STORAGE_ACCOUNT_NAME + ".blob.core.windows.net",
mount_point = "/mnt/TP",
extra_configs = {"fs.azure.account.key." + STORAGE_ACCOUNT_NAME + ".blob.core.windows.net":dbutils.secrets.get(scope = SCOPE, key = STORAGE_ACCOUNT_KEY)})
