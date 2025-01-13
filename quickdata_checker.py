# Shape: Displays the shape of the DataFrame.
# Types: Displays the data types of each column.
# Head: Displays the first few rows of the DataFrame.
# Tail: Displays the last few rows of the DataFrame.
# NA: Displays the count of missing values in each column.
# NA Percentage: Displays the percentage of missing values in each column.
# Unique Values: Displays the number of unique values in each column.
# Quantiles: Displays the quantiles of numerical columns.
# Correlation Matrix: Displays the correlation matrix for numerical columns.
# Value Counts: Displays the value counts for categorical columns.
# Memory Usage: Displays the memory usage of the DataFrame.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    
    print("##################### Types #####################")
    print(dataframe.dtypes)
    
    print("##################### Head #####################")
    print(dataframe.head(head))
    
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    
    print("##################### NA Percentage #####################")
    print((dataframe.isnull().sum() / len(dataframe) * 100).round(2))
    
    print("##################### Unique Values #####################")
    print(dataframe.nunique())
    
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    
    print("##################### Correlation Matrix #####################")
    numeric_cols = dataframe.select_dtypes(include=['number']).columns
    print(dataframe[numeric_cols].corr())
    
    print("##################### Value Counts #####################")
    for column in dataframe.select_dtypes(include=['object', 'category']).columns:
        print(f"##################### {column} #####################")
        print(dataframe[column].value_counts())
    
    print("##################### Memory Usage #####################")
    print(dataframe.memory_usage(deep=True))

# Example usage:
df = sns.load_dataset("titanic")
check_df(df)

# Example usage:
# import pandas as pd or
# import seaborn as sns
# df = pd.read_csv('your_data.csv')
# df = sns.load_dataset("your_data")
# check_df(df)

