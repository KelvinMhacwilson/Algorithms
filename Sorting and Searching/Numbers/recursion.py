def addition(numbers):
  if not numbers:
    return 0
  
  remaining_sum = sum(numbers[1:])
  print(remaining_sum)
  return numbers[0] + remaining_sum

print(addition([1, 2, 7,9]))