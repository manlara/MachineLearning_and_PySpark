# Databricks notebook source
dbutils.library.installPyPI("koalas")
dbutils.library.restartPython()

# COMMAND ----------

import databricks.koalas as ks
import pandas as pd

pdf = pd.DataFrame({'x':range(3), 'y':['a','b','b'], 'z':['a','b','b']})

# Create a Koalas DataFrame from pandas DataFrame
df = ks.from_pandas(pdf)

# Rename the columns
df.columns = ['x', 'y', 'z1']

# Do some operations in place:
df['x2'] = df.x * df.x

# COMMAND ----------


