from operator import index

''' Returns the index position of the target if found, else returns None '''
def linear_search(list, target):

  for i in range(0, len(list)):
    if list [i] == target:
      return i
  return None

''' Prints the target's index, if existent '''
def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in the list")

''' Array of numbers to loop '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)