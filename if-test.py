leaves_on_the_tree = 2

if leaves_on_the_tree == 0:
  print("It must be winter — or a dead tree")
else:
  print("It is summer")

def get_highest_number(a, b):
  if a>b:
    return a
  else:
    return b
  
print(f"Highest number: {get_highest_number(1,5)} (should be 5)")
print(f"Highest number: {get_highest_number(10,5)} (should be 10)")

def text_includes_word(text, word):
  if word in text:
    return True
  else:
    return False
  
print(text_includes_word("I am here.", "here"))
print(text_includes_word("I am here.", "home"))