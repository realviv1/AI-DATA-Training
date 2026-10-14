import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
"Employee": ["Aisha", "Rahul", "Neha", "Omar", "Priya", "Karan", "Fatima", "Vikram"],
"Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR"],
"Training_Hours": [12, 18, 10, 22, 15, 8, 20, 14],
"Assessment_Score": [78, 88, 72, 91, 84, 69, 95, 80],
"Completed": ["Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes"]
}
df = pd.DataFrame(data)
print(df)
print(df.head(4))
print(df[['Employee', 'Assessment_Score']])
print(df[df["Department"] == "IT"])
print(df[df["Assessment_Score"] > 80])
print(df[df["Completed"] == "Yes"])

it_high_score = df[
(df['Department'] == 'IT') &
(df['Assessment_Score'] > 85)
]
print(it_high_score)

df["Passed"] = np.where(df["Assessment_Score"] >= 75, 'Pass', 'Fail')
print(df["Assessment_Score"].mean())
print('Maximum:', np.max(df["Assessment_Score"]))
print('Minimum:', np.min(df["Assessment_Score"]))
avg_training_hours = df['Training_Hours'].mean()
print("Average Training Hours:", avg_training_hours)
sorted_df = df.sort_values(by='Assessment_Score', ascending=False)

print(sorted_df)
avg_score_dept = df.groupby('Department')["Assessment_Score"].mean()
print(avg_score_dept)

total_hours_dept = df.groupby("Department")["Training_Hours"].sum()
print(total_hours_dept)

employee_count = df['Department'].value_counts()
print(employee_count)

completion_count = df['Completed'].value_counts()
print(completion_count)

scores = df['Assessment_Score'].to_numpy()
print("Mean:", np.mean(scores))
print("Maximum:", np.max(scores))
print("Minimum:", np.min(scores))
print("Standard Deviation:", np.std(scores))


avg_score_dept = df.groupby('Department')['Assessment_Score'].mean()
plt.figure(figsize=(8,5))
avg_score_dept.plot(kind='bar', color='skyblue')
plt.title('Average Assessment Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.show()


total_hours_dept = df.groupby('Department')['Training_Hours'].sum()
plt.figure(figsize=(8,5))
total_hours_dept.plot(kind='bar', color='green')
plt.title('Total Training Hours by Department')
plt.xlabel('Department')
plt.ylabel('Training Hours')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x='Department',
    y='Assessment_Score'
)

plt.title('Department vs Assessment Score')
plt.xlabel('Department')
plt.ylabel('Assessment Score')

plt.show()

