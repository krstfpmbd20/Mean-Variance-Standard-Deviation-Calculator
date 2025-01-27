import pyspark
from pyspark.sql import SparkSession
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName('Practice').getOrCreate()

# Read CSV file into PySpark DataFrame
df_pyspark = spark.read.csv('Excel Projects/advertising.csv', header=True, inferSchema=True)

# Show the DataFrame
df_pyspark.show()