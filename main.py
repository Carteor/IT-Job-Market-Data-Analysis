import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data.isnull().sum())
print("Performing data cleanup")

data['salary_missing'] = data['salary'].isnull().astype(int)

data['salary'].fillna(-1, inplace=True)
data['salary'] = pd.to_numeric(data['salary'], errors='coerce')
data['salary'].fillna(-1, inplace=True)

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

# Histogram for the salary column
plt.hist(data['salary'], bins=30, edgecolor='black')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()