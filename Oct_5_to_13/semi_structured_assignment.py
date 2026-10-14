import json
import pandas as pd

with open("festival_events.json", "r") as file:
    data = json.load(file)

print("Event Names:")
for event in data:
    print(event['name'])

print("\nCities:")
for event in data:
    print(event['location']['city'])

print("\nVisitors > 700:")
for event in data:
    if event['visitors'] > 700:
        print(event['name'])

print("\nFeatures:")
for event in data:
    print(event['name'])

    if 'features' in event:
        print(event['features'])
    else:
        print("No features listed")

df = pd.json_normalize(data)

print("\nDataFrame:")
print(df)