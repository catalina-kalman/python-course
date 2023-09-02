my_dictionary = {
  "String": "A sequence of characters",
  "List": "A sequence of any item",
  "Dictionary": "Key value pairs"
}

print(my_dictionary["List"])

words = ["hat", "cat", "I", "bird"]

def count_words_by_length(words):
  word_dictionary = {}
  for word in words:
    if len(word) in word_dictionary:
      word_dictionary[len(word)] += 1
    else:
       word_dictionary[len(word)] = 1
  return word_dictionary
  
print(count_words_by_length(words))