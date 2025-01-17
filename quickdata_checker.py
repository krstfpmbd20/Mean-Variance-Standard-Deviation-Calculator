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
    
    print("##################### Unique Values #####################")
    print(dataframe.nunique())
    
    print("##################### Suspicious or Wrong Data #####################")
    detect_suspicious_data(dataframe)
    
    print("##################### Memory Usage #####################")
    print(dataframe.memory_usage(deep=True))

# Example usage:
if __name__ == "__main__":
    # Load a sample dataset
    df = pd.read_csv("cleaned_lung_cancer_data.csv")
    check_df(df)