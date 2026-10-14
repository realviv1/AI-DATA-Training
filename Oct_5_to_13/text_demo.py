with open("incident_notes.txt") as file:
    text = file.read()

print(text)

words = text.split()
print("Total words:", len(words))

if "vibration" in text.lower():
    print("Vibration was mentioned")

print(text.lower().count("vibration"))
