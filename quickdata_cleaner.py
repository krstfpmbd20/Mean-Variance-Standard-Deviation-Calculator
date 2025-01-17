import pandas as pd

def load_dataset(file_path):
    return pd.read_csv(file_path)

def save_dataset(df, file_path):
    df.to_csv(file_path, index=False)

def drop_missing_values(df):
    return df.dropna()

def fill_missing_values(df, value):
    return df.fillna(value)

def remove_duplicates(df):
    return df.drop_duplicates()

def convert_to_datetime(df, columns):
    for column in columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def strip_whitespace(df):
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def quick_clean(df, fill_value=None, datetime_columns=None):
    print("Starting quick data cleaning...")
    
    # Drop missing values
    df = drop_missing_values(df)
    print("Dropped missing values.")
    
    # Fill missing values if fill_value is provided
    if fill_value is not None:
        df = fill_missing_values(df, fill_value)
        print(f"Filled missing values with {fill_value}.")
    
    # Remove duplicates
    df = remove_duplicates(df)
    print("Removed duplicates.")
    
    # Convert specified columns to datetime
    if datetime_columns is not None:
        df = convert_to_datetime(df, datetime_columns)
        print(f"Converted columns {datetime_columns} to datetime.")
    
    # Strip whitespace from string columns
    df = strip_whitespace(df)
    print("Stripped whitespace from string columns.")
    
    print("Data cleaning completed.")
    return df

# Example usage:
if __name__ == "__main__":
    input_file = "path/to/your/input.csv"
    output_file = "path/to/your/output.csv"
    
    # Load dataset
    df = load_dataset(input_file)
    
    # Perform quick cleaning
    cleaned_df = quick_clean(df, fill_value=0, datetime_columns=['date_column'])
    
    # Save cleaned dataset
    save_dataset(cleaned_df, output_file)
    print(f"Cleaned dataset saved to {output_file}.")