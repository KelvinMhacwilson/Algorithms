def merge_sort(list):
  """
  Sorts a list in ascending order
  REturns the new sorted list

  Divide: Find the midpoint of the list and divide subLists
  Conquer: Recursively sort the subLists created in previous step
  Combine: Merge the sorted subLists created in previous step
  Takes overall O(kn log n) time
  """
  if len(list) <=1:
    return list
  
  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(list):
  """
  Divide the unsorted list at midpoint into sublists
  Returns two sublists - left and right

  Takes overall O(k log n) time
  """

  mid =len(list) // 2
  left = list[:mid]
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Mergers two lists, sorting them in the process
  Returns a new merged list
  Takes overall O(n) time
  """
  l = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1

  while i < len(left):
    l.append(left[i])
    i+=1

  while j < len(right):
    l.append(right[j])
    j+=1
  
  return l
  
a_list = [54, 31, 12,14,18,50,74, 18,17, 8, 50]

def verify_sorted(list):
  n = len(list)

  if n == 0 or n == 1:
    return True
  
  return list[0] < list[1] and verify_sorted(list[1:])
  # not working re-check it again 

# print(verify_sorted(a_list))
list = merge_sort(a_list)
print(list)
print(verify_sorted(list))

# Write without recursion

