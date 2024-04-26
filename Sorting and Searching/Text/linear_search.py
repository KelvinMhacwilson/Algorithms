search_names = ["Kelvin", "Dart", "Bart", "Priscilla", "Michelle", "Solomon", "Paul","John", "Peter", "Sally", "Samuel"]

def index_of_item(collection, target):
  for i in range(0, len(collection)):
    if target == collection[i]:
      return i
  return None


names = ["Sampson", "Dart", "Bart", "Priscilla", "Michelle", "Solomon", "Paul","John", "Peter", "Sally", "Samuel","Kelvin"]

for n in search_names:
  index = index_of_item(names, n)
  print(index)