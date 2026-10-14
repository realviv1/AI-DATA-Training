import pandas as pd

df = pd.read_csv("structured_data.csv")

print("\n1. Complete Data")
print(df)

print("\n2. Shipment_ID, Origin, Destination, Cost")
print(df[["Shipment_ID", "Origin", "Destination", "Cost"]])

print("\n3. Road Shipments")
print(df[df["Mode"] == "Road"])

print("\n4. Weight > 150")
print(df[df["Weight_Kg"] > 150])

df["Cost_Per_Km"] = df["Cost"] / df["Distance_Km"]

print("\n5. Cost Per Km")
print(df[["Shipment_ID", "Cost_Per_Km"]])

print("\n6. Cost Statistics")
print("Average Cost:", df["Cost"].mean())
print("Highest Cost:", df["Cost"].max())
print("Lowest Cost:", df["Cost"].min())

print("\n7. Total Cost by Mode")
print(df.groupby("Mode")["Cost"].sum())

print("\n8. Average Weight by Mode")
print(df.groupby("Mode")["Weight_Kg"].mean())

print("\n9. Highest to Lowest Cost")
print(df.sort_values(by="Cost", ascending=False))

print("\n10. Delivery <=1 and Cost <5000")
print(df[(df["Delivery_Days"] <= 1) & (df["Cost"] < 5000)])

