# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]
list_to_be_filtered = [1, 2, 3, 4, 5]

def find_odds(numbers):
  if not numbers:
    return []
  if numbers[0] % 2 == 1:
    return [numbers[0]] + find_odds(numbers[1:])
  return find_odds(numbers[1:])

print(find_odds(list_to_be_filtered))