import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')

print(data.isnull().sum())
print("Performing data cleanup")

data['salary_missing'] = data['salary'].isnull().astype(int)

data['currency'] = data['salary'].str.extract(r'([A-Za-z]+)')

unique_currencies = data['currency'].unique()
print(unique_currencies)

data['numeric_salary'] = data['salary'].str.replace(r'[^\d]', '', regex=True).astype(float)
#data['salary'].fillna(-1, inplace=True)



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

# Boxplot for each currency
plt.figure(figsize=(12,8))
sns.boxplot(x='currency', y='numeric_salary', data=data)
plt.title('Salary Distribution by Currency')
plt.ylabel('Salary')
plt.xlabel('Currency')
plt.show()