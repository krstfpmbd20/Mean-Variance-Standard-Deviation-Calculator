import pandas as pd

# Data dictionary
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

# Creating the DataFrame
df = pd.DataFrame(data)

# 1. How many of each race are represented in this dataset?
race_count = df['race'].value_counts()
print("Race count:\n", race_count)

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print("Average age of men:", round(average_age_men, 1))

# 3. Percentage of people with Bachelor's degree
percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
print("Percentage with Bachelor's degree:", round(percentage_bachelors, 1))

# 4. Percentage of people with advanced education (Bachelors, Masters, Doctorate) making more than 50K
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
higher_education = df[df['education'].isin(advanced_education)]
higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
print("Percentage with advanced education and earning >50K:", round(higher_education_rich, 1))

# 5. Percentage of people without advanced education making more than 50K
lower_education = df[~df['education'].isin(advanced_education)]
lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100
print("Percentage without advanced education and earning >50K:", round(lower_education_rich, 1))

# 6. Minimum number of hours a person works per week
min_work_hours = df['hours-per-week'].min()
print("Minimum work hours per week:", min_work_hours)

# 7. Percentage of people who work the minimum hours and earn more than 50K
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100 if num_min_workers.shape[0] > 0 else 0
print("Percentage of people who work minimum hours and earn >50K:", round(rich_percentage, 1))

# 8. Country with the highest percentage of people that earn >50K
country_salary_df = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size()

if country_salary_df.dropna().empty:
    highest_earning_country = None
    highest_earning_country_percentage = 0
else:
    highest_earning_country = country_salary_df.idxmax()
    highest_earning_country_percentage = country_salary_df.max() * 100

print("Country with highest percentage earning >50K:", highest_earning_country)
print("Percentage of people in that country earning >50K:", round(highest_earning_country_percentage, 1))

# 9. Most popular occupation for those who earn >50K in India
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax() if not df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].empty else None
print("Most popular occupation in India for those earning >50K:", top_IN_occupation)
