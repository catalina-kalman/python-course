def get_nth_character(text, place):
    char = text[place - 1]
    return char

text = "This is a sentence."

print(text[-1])
print(text[0])
print(text[1])

print(text[0:4])

print(f"Function: {get_nth_character(text, 3)}")