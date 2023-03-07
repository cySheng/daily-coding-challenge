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