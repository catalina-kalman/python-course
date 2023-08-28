text = "My name is my_name"

print(f"Lenght of string: {len(text)}")

text = text.replace("my_name", "Kay")
print(f"Replace text: {text}")

print(f"All uppercase: {text.upper()}")

print(f"All lowercase: {text.lower()}")

print("Concat: " + text + ".")

print("Concat a number: " + text + str(2))