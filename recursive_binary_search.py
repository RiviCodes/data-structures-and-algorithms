from unicodedata import numeric


def recursive_binary_search(list, target):
  ''' Check if list is empty '''
  if len(list) == 0:
    return False
  else:
    midpoint = (len(list)) // 2

    '''First check'''
    if list[midpoint] == target:
      return True
    else:
      ''' Here is another check '''
      if list[midpoint] < target:
        return recursive_binary_search(list[midpoint + 1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

def verify(result):
  print('Target found: ', result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

'''Testing'''
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)