def add_cats_repeatedly(count):
  word_list = []
  i = 0
  while i<count:
    word_list = word_list + ["cat"]
    i = i + 1
  return word_list

print(add_cats_repeatedly(4))