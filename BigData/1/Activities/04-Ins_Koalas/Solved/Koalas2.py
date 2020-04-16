#!/usr/bin/env python
# coding: utf-8

# # 10 minutes to Koalas
# 
# This is a short introduction to Koalas, geared mainly for new users. This notebook shows you some key differences between pandas and Koalas. You can run this examples by yourself on a live notebook [here](https://mybinder.org/v2/gh/databricks/koalas/master?filepath=docs%2Fsource%2Fgetting_started%2F10min.ipynb). For Databricks users, you can import [the current .ipynb file](https://raw.githubusercontent.com/databricks/koalas/master/docs/source/getting_started/10min.ipynb) and run it after [installing Koalas](https://github.com/databricks/koalas#how-do-i-use-this-on-databricks).
# 
# Customarily, we import Koalas as follows:

# COMMAND ----------


import pandas as pd
import numpy as np
import databricks.koalas as ks
from pyspark.sql import SparkSession


# ## Object Creation
# 
# 

# Creating a Koalas Series by passing a list of values, letting Koalas create a default integer index:

# COMMAND ----------


s = ks.Series([1, 3, 5, np.nan, 6, 8])


# COMMAND ----------


s


# Creating a Koalas DataFrame by passing a dict of objects that can be converted to series-like.

# COMMAND ----------


kdf = ks.DataFrame(
    {'a': [1, 2, 3, 4, 5, 6],
     'b': [100, 200, 300, 400, 500, 600],
     'c': ["one", "two", "three", "four", "five", "six"]},
    index=[10, 20, 30, 40, 50, 60])


# COMMAND ----------


kdf


# Creating a pandas DataFrame by passing a numpy array, with a datetime index and labeled columns:

# COMMAND ----------


dates = pd.date_range('20130101', periods=6)


# COMMAND ----------


dates


# COMMAND ----------


pdf = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))


# COMMAND ----------


pdf


# Now, this pandas DataFrame can be converted to a Koalas DataFrame

# COMMAND ----------


kdf = ks.from_pandas(pdf)


# COMMAND ----------


type(kdf)


# It looks and behaves the same as a pandas DataFrame though

# COMMAND ----------


kdf


# Also, it is possible to create a Koalas DataFrame from Spark DataFrame.  
# 
# Creating a Spark DataFrame from pandas DataFrame

# COMMAND ----------


spark = SparkSession.builder.getOrCreate()


# COMMAND ----------


sdf = spark.createDataFrame(pdf)


# COMMAND ----------


sdf.show()


# Creating Koalas DataFrame from Spark DataFrame.
# `to_koalas()` is automatically attached to Spark DataFrame and available as an API when Koalas is imported.

# COMMAND ----------


kdf = sdf.to_koalas()


# COMMAND ----------


kdf


# Having specific [dtypes](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-dtypes) . Types that are common to both Spark and pandas are currently supported.

# COMMAND ----------


kdf.dtypes


# ## Viewing Data
# 
# See the [API Reference](https://koalas.readthedocs.io/en/latest/reference/index.html).

# See the top rows of the frame. The results may not be the same as pandas though: unlike pandas, the data in a Spark dataframe is not _ordered_, it has no intrinsic notion of index. When asked for the head of a dataframe, Spark will just take the requested number of rows from a partition. Do not rely on it to return specific rows, use `.loc` or `iloc` instead.

# COMMAND ----------


kdf.head()


# Display the index, columns, and the underlying numpy data.
# 
# You can also retrieve the index; the index column can be ascribed to a DataFrame, see later

# COMMAND ----------


kdf.index


# COMMAND ----------


kdf.columns


# COMMAND ----------


kdf.to_numpy()


# Describe shows a quick statistic summary of your data

# COMMAND ----------


kdf.describe()


# Transposing your data

# COMMAND ----------


kdf.T


# Sorting by its index

# COMMAND ----------


kdf.sort_index(ascending=False)


# Sorting by value

# COMMAND ----------


kdf.sort_values(by='B')


# ## Missing Data
# Koalas primarily uses the value `np.nan` to represent missing data. It is by default not included in computations. 
# 

# COMMAND ----------


pdf1 = pdf.reindex(index=dates[0:4], columns=list(pdf.columns) + ['E'])


# COMMAND ----------


pdf1.loc[dates[0]:dates[1], 'E'] = 1


# COMMAND ----------


kdf1 = ks.from_pandas(pdf1)


# COMMAND ----------


kdf1


# To drop any rows that have missing data.

# COMMAND ----------


kdf1.dropna(how='any')


# Filling missing data.

# COMMAND ----------


kdf1.fillna(value=5)


# ## Operations

# ### Stats
# Operations in general exclude missing data.
# 
# Performing a descriptive statistic:

# COMMAND ----------


kdf.mean()


# ### Spark Configurations
# 
# Various configurations in PySpark could be applied internally in Koalas.
# For example, you can enable Arrow optimization to hugely speed up internal pandas conversion. See <a href="https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html">PySpark Usage Guide for Pandas with Apache Arrow</a>.

# COMMAND ----------


prev = spark.conf.get("spark.sql.execution.arrow.enabled")  # Keep its default value.
ks.set_option("compute.default_index_type", "distributed")  # Use default index prevent overhead.
import warnings
warnings.filterwarnings("ignore")  # Ignore warnings coming from Arrow optimizations.


# COMMAND ----------


spark.conf.set("spark.sql.execution.arrow.enabled", True)
get_ipython().run_line_magic('timeit', 'ks.range(300000).to_pandas()')


# COMMAND ----------


spark.conf.set("spark.sql.execution.arrow.enabled", False)
get_ipython().run_line_magic('timeit', 'ks.range(300000).to_pandas()')


# COMMAND ----------


ks.reset_option("compute.default_index_type")
spark.conf.set("spark.sql.execution.arrow.enabled", prev)  # Set its default value back.


# ## Grouping
# By “group by” we are referring to a process involving one or more of the following steps:
# 
# - Splitting the data into groups based on some criteria
# - Applying a function to each group independently
# - Combining the results into a data structure

# COMMAND ----------


kdf = ks.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})


# COMMAND ----------


kdf


# Grouping and then applying the [sum()](https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.groupby.GroupBy.sum.html#databricks.koalas.groupby.GroupBy.sum) function to the resulting groups.

# COMMAND ----------


kdf.groupby('A').sum()


# Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.

# COMMAND ----------


kdf.groupby(['A', 'B']).sum()


# ## Plotting
# See the <a href="https://koalas.readthedocs.io/en/latest/reference/frame.html#plotting">Plotting</a> docs.

# COMMAND ----------


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt


# COMMAND ----------


pser = pd.Series(np.random.randn(1000),
                 index=pd.date_range('1/1/2000', periods=1000))


# COMMAND ----------


kser = ks.Series(pser)


# COMMAND ----------


kser = kser.cummax()


# COMMAND ----------


kser.plot()


# On a DataFrame, the <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.frame.DataFrame.plot.html#databricks.koalas.frame.DataFrame.plot">plot()</a> method is a convenience to plot all of the columns with labels:

# COMMAND ----------


pdf = pd.DataFrame(np.random.randn(1000, 4), index=pser.index,
                   columns=['A', 'B', 'C', 'D'])


# COMMAND ----------


kdf = ks.from_pandas(pdf)


# COMMAND ----------


kdf = kdf.cummax()


# COMMAND ----------


kdf.plot()


# ## Getting data in/out
# See the <a href="https://koalas.readthedocs.io/en/latest/reference/io.html">Input/Output
# </a> docs.

# ### CSV
# 
# CSV is straightforward and easy to use. See <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.DataFrame.to_csv.html#databricks.koalas.DataFrame.to_csv">here</a> to write a CSV file and <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.read_csv.html#databricks.koalas.read_csv">here</a> to read a CSV file.

# COMMAND ----------


kdf.to_csv('foo.csv')
ks.read_csv('foo.csv').head(10)


# ### Parquet
# 
# Parquet is an efficient and compact file format to read and write faster. See <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.DataFrame.to_parquet.html#databricks.koalas.DataFrame.to_parquet">here</a> to write a Parquet file and <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.read_parquet.html#databricks.koalas.read_parquet">here</a> to read a Parquet file.

# COMMAND ----------


kdf.to_parquet('bar.parquet')
ks.read_parquet('bar.parquet').head(10)


# ### Spark IO
# 
# COMMAND ----------

# COMMAND ----------


kdf.to_spark_io('zoo.orc', format="orc")
ks.read_spark_io('zoo.orc', format="orc").head(10)

