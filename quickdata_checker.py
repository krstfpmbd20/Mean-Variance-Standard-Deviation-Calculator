import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def check_df(df, head=5):
    print("##################### Shape #####################")
    print(df.shape)
    
    print("##################### Types #####################")
    print(df.dtypes)
    
    print("##################### Head #####################")
    print(df.head(head))
    
    print("##################### Tail #####################")
    print(df.tail(head))
    
    print("##################### NA #####################")
    print(df.isnull().sum())
    
    print("##################### Unique Values #####################")
    print(df.nunique())
    
    print("##################### Memory Usage #####################")
    print(df.memory_usage(deep=True))

# Example usage:
if __name__ == "__main__":
    # Load a sample dataset
    df = pd.read_csv("cleaned_lung_cancer_data.csv")
    check_df(df)