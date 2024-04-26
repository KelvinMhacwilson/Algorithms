import random
import sys

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  attempts = 0

  while not is_sorted(values):
    print(attempts)
    random.shuffle(values)
    attempts = attempts + 1
  return values


numbers = [1,10,3,4,2]
print(bogo_sort(numbers))