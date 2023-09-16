import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')

print(data.isnull().sum())
print("Performing data cleanup")

data['salary_missing'] = data['salary'].isnull().astype(int)

data['currency'] = data['salary'].str.extract(r'([A-Za-z]+)')

unique_currencies = data['currency'].dropna().unique()
print(unique_currencies)

data['salary'] = data['salary'].astype(str)
print(data[data['currency'] == 'KZT']['salary'].head(10))
# When dealing with range salary like 500 000 - 600 000 KZT
# Extract the max and min values
data['min_salary_extracted'] = data['salary'].str.extract(r'(\d+(?:\s\d+)*)[^\d]+')
data['max_salary_extracted'] = data['salary'].str.extract(r'(\d+(?:\s\d+)*)(?=[^\d]*[A-Za-z])')
# Remove spaces and convert to floats
data['min_salary'] = data['min_salary_extracted'].str.replace("\s", "").astype(float)
data['max_salary'] = data['max_salary_extracted'].str.replace("\s", "").astype(float)
print(data[data['currency'] == 'KZT'][['salary', 'max_salary']].head(10))

data['max_salary'].fillna(data['min_salary'], inplace=True)
print(data[data['currency'] == 'KZT'][['salary', 'min_salary', 'max_salary']].head(10))

# calculate the average to get representative salary
data['avg_salary'] = data[['min_salary', 'max_salary']].mean(axis=1)
data['avg_salary'].fillna(data['min_salary'], inplace=True)
print(data[data['currency'] == 'KZT'][['salary', 'min_salary', 'max_salary', 'avg_salary']].head(10))

data['requirements'].fillna('Not Specified', inplace=True)
data['responsibilities'].fillna('Not Specified', inplace=True)

data['schedule'].fillna(-1, inplace=True)

data['publish_date'] = pd.to_datetime(data['publish_date'], format='%d-%m-%Y')

print("Results:", data.isnull().sum())

# Summary statistics
numerical_summary = data.describe()
print(numerical_summary)

categorical_summary = data.describe(include="object")
print(categorical_summary)

# Boxplot for each currency 'KZT' 'RUR' 'USD' 'EUR'
plt.figure(figsize=(15, 10))

for idx, currency in enumerate(unique_currencies, 1):
    plt.subplot(2,2,idx)
    sns.histplot(data[data['currency'] == currency]['avg_salary'],bins=50,kde=True,color='purple')
    plt.title(f'Average Salary Distribution ({currency})')
    plt.ylabel('Frequency')
    plt.xlabel('Average Salary')

plt.tight_layout()
plt.show()
