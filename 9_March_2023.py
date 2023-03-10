# [Hard]
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

# import the builtin time module
import time

x = [3, 4, -1, 1, 1, 5, 5, 7, 2]

y = [1, 2, 0, 3, 4]

# Test Memory Usage
# 1. To test memory usage, install memory profiler, 'pip install -U memory_profiler'
# 2. Uncomment the @profile line below
# 3. Run 'python -m memory_profiler 9_March_2023.py'

# @profile
def find_missing_integer(input):
  input[:] = [*set(x for x in input if x != 0 and x > 0 and x < len(input))]
  input[:] = [-x if x < len(input) else x for x in input]
  for x in input:
    if x < 0:
      continue
    elif x == len(input):
      return x + 1
    elif x > len(input):
      return x - 1

  return input


print(find_missing_integer(x))
print(find_missing_integer(y))


time_to_run = 1000000

# Grab Currrent Time Before Running the Code
start = time.time()

for a in range(time_to_run):
  find_missing_integer(x)

# Grab Currrent Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
average_time = (end - start)/time_to_run
print("With an array of 8 inputs, it took: "+ str(average_time))


# Grab Currrent Time Before Running the Code
start = time.time()

for a in range(time_to_run):
  find_missing_integer(y)

# Grab Currrent Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
average_time = (end - start)/time_to_run
print("With an array of 4 inputs, it took: "+ str(average_time))
