

with open("unstructured_data.txt", "r") as file:
    text = file.read()

print("\n1. Complete Text")
print(text)

words = text.split()
print("\n2. Total Words:", len(words))


with open("unstructured_data.txt", "r") as file:
    lines = file.readlines()

print("\n3. Total Lines:", len(lines))


print("\n4. maintenance exists?")
if "maintenance" in text.lower():
    print("Found")
else:
    print("Not Found")


print("\n5. Conveyor Count")
print(text.lower().count("conveyor"))

# 6. Lines containing team

print("\n6. Lines with team")

for line in lines:
    if "team" in line.lower():
        print(line.strip())

# 7. Lines containing incident

print("\n7. Lines with incident")

for line in lines:
    if "incident" in line.lower():
        print(line.strip())


print("\n8. Damaged Component")

for line in lines:
    if "damaged" in line.lower():
        print(line.strip())


with open("lowercase_report.txt", "w") as file:
    file.write(text.lower())

print("\n9. lowercase_report.txt created")


print("\n10. Keyword Summary")

keywords = [
    "maintenance",
    "injuries",
    "inspection",
    "replacement",
    "operations"
]

for word in keywords:
    if word in text.lower():
        print(f"{word:<12} : Found")
    else:
        print(f"{word:<12} : Not Found")