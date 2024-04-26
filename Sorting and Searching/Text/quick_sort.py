numbers = [4,6,3,2,9,7,3,5]

def quick_sort(values):
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot=values[0]

  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  
  return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# python quick_sort.py > SortedNames.txt
# Sort Names
names = ["Sampson", "Dart", "Bart", "Priscilla", "Michelle", "Solomon", "Paul","John", "Peter", "Sally", "Samuel","Kelvin"]
sorted_names= quick_sort(names)
SortedNames = []
for n in sorted_names:
  SortedNames.append(n)
  # print(n)
print(SortedNames)