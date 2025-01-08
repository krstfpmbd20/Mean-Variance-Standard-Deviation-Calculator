import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.columns = df.columns.str.capitalize()
df['Age'] = df['Age'].fillna(0).astype(int)
df['Sex'] = df['Sex'].str.capitalize()
df['Who'] = df['Who'].str.capitalize()
df['Alive'] = df['Alive'].str.capitalize()
df['Survived'] = df['Survived'].map({1: 'Yes', 0: 'No'})
df['Class'] = df['Class'].map({'Third': '3rd', 'First': '1st', 'Second': '2nd'})
df['Deck'] = df['Deck'].astype('category')
df['Deck'] = df['Deck'].cat.add_categories('Unknown').fillna('Unknown')
df['Alone'] = df['Alone'].map({False: 'No', True: 'Yes'})
df['Embarked'] = df['Embarked'].fillna('Unknown')
df['Embark_town'] = df['Embark_town'].fillna('Unknown')
df = df.drop(columns=['Who'])
df = df.rename(columns={'Adult_male': 'Adult_status'})
df['Adult_status'] = df['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Child')

# Plot the number of survivors and casualties
survival_counts = df['Survived'].value_counts()
ax = survival_counts.plot(kind='bar', color=['red', 'green'])
plt.title('Number of Survivors and Casualties')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks(rotation=0)
for i in ax.containers:
    ax.bar_label(i)
plt.savefig('Titanic Dataset/survivors_and_casualties.png')  # Save the plot as a PNG file
#plt.show()

# Plot the number of survivors by sex
survival_by_sex = df.groupby(['Sex', 'Survived']).size().unstack()
ax = survival_by_sex.plot(kind='bar', stacked=False, color=['red', 'green'])
plt.title('Gender of Survivors and Casualties')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
for i in ax.containers:
    ax.bar_label(i)
plt.savefig('Titanic Dataset/survivors_by_sex.png')  # Save the plot as a PNG file
#plt.show()

# Plot the number of survivors by adult status
survival_by_adult_status = df.groupby(['Adult_status', 'Survived']).size().unstack()
ax = survival_by_adult_status.plot(kind='bar', stacked=False, color=['red', 'green'])
plt.title('Number of Survivors by Adult Status')
plt.xlabel('Adult Status')
plt.ylabel('Count')
plt.xticks(rotation=0)
for i in ax.containers:
    ax.bar_label(i)
plt.savefig('Titanic Dataset/survivors_by_adult_status.png')  # Save the plot as a PNG file
#plt.show()

# Print the results
#print(df.head())
#print(df['Survived'].value_counts())

df.to_excel('Titanic Dataset/cleaned_titanic_dataset.xlsx', index=False)