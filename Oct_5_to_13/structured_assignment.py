import pandas as pd

df = pd.read_csv("library_loans.csv")

print("Selected Columns:")
print(df[['Member_Name', 'Book_Category', 'Fine']])

print("\nFine Greater Than 50:")
print(df[df['Fine'] > 50])

df['Status'] = df['Fine'].apply(
    lambda x: 'No Fine' if x == 0 else 'Fine Due'
)

print("\nData with Status:")
print(df)

avg_days = df['Days_Borrowed'].mean()
print("\nAverage Days Borrowed:", avg_days)

fine_by_category = df.groupby('Book_Category')['Fine'].sum()

print("\nTotal Fine by Category:")
print(fine_by_category)


