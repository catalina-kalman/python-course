words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again

for word in words: # We go through each word
  first_letter = word[0] # Get the first letter
  # And append it to our accumulator list:
  first_letters.append(first_letter)

print(words)
print(first_letters)

number_list = [1, 2, 3, 4, 5]

def add_one_hundred_to_numbers(numbers):
  numbers_add = []
  for number in numbers:
    numbers_add.append(number + 100)
  return numbers_add

print(add_one_hundred_to_numbers(number_list))