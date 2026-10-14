with open("wildlife_report.txt", "r") as file:
    content = file.read()

print("Complete Report:")
print(content)

word_count = len(content.split())

print("\nTotal Words:", word_count)

if "elephant" in content.lower():
    print("\nWord 'elephant' found")
else:
    print("\nWord 'elephant' not found")

count = content.lower().count("elephant")

print("Occurrences of 'elephant':", count)

print("\nLines containing 'trail':")

with open("wildlife_report.txt", "r") as file:
    for line in file:
        if "trail" in line.lower():
            print(line.strip())

print("\nLines containing 'animal':")

with open("wildlife_report.txt", "r") as file:
    for line in file:
        if "animal" in line.lower():
            print(line.strip())