import pandas as pd

# Load your dataset
df = pd.read_csv("Excel Projects/incomes.csv")

# Count all "?" values in the WorkLevel column
question_mark_count = (df["WorkLevel"] == "?").sum()

print(f'Total number of "?" values in the WorkLevel column: {question_mark_count}')