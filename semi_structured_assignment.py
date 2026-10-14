import json
import pandas as pd
with open("semi_structured_data.json", "r") as file:
    incidents = json.load(file)

print("\n2. Incident IDs")
for incident in incidents:
    print(incident["incident_id"])

print("\n3. Cities")
for incident in incidents:
    print(incident["location"]["city"])

print("\n4. High Severity")
for incident in incidents:
    if incident["severity"] == "High":
        print(incident)

print("\n5. Safety Category")
for incident in incidents:
    if incident["category"] == "Safety":
        print(incident)

print("\n6. Actions")
for incident in incidents:
    print(incident["incident_id"])
    if "actions" in incident:
        print(incident["actions"])
    else:
        print("No actions recorded")

print("\n7. Severity Count")

severity_count = {}

for incident in incidents:
    severity = incident["severity"]

    if severity in severity_count:
        severity_count[severity] += 1
    else:
        severity_count[severity] = 1

print(severity_count)

for incident in incidents:
    incident["status"] = "Open"

with open("updated_incidents.json", "w") as file:
    json.dump(incidents, file, indent=4)

print("\nUpdated file saved")

print("\n10. JSON Normalize")

df = pd.json_normalize(incidents)

print(
    df[
        [
            "incident_id",
            "severity",
            "category",
            "location.city",
            "location.site",
        ]
    ]
)