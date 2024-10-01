import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("demographic.csv")

    # 1. How many people of each race are represented in this dataset? (race column)
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    # Advanced education
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    # People with advanced education and salary > 50K
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    # Without advanced education
    lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    # People without advanced education and salary > 50K
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_min_workers = round((df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / country_count * 100).idxmax()
    highest_earning_country_percentage = round((country_earnings / country_count * 100).max(), 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_min_workers}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }