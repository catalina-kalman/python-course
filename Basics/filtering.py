numbers = [-4, 4, -3, 3, 0]

def only_positive_numbers(numbers):
  positive_numbers = []
  for number in numbers:
    if number > 0:
      positive_numbers.append(number)
  return positive_numbers

print(only_positive_numbers(numbers))