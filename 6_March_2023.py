# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


numbers = [10, 15, 3, 2, 18, 20, 100, 105, 300, 500, 6, 1]
k = 17

# multiple passes
def evaluate_k(number, array):
  for index_one, i in enumerate(array):
    for index_two, j in enumerate(array):
      if index_one >= index_two:
        continue
      else:
        if i + j == k:
          return True
  return False

# one pass
def pro_evaluate_k(number, array):
  for index, i in enumerate(array):
    leftover = number - i
    if leftover in array and array.index(leftover): return True
  return False



print(evaluate_k(k, numbers))
print(pro_evaluate_k(k, numbers))