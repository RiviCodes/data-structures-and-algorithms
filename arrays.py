new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
  if n == 1:
    print(True)

    break

numbers = [4, 5, 6]

new_list.extend(numbers)
'''Prints [1, 2, 3, 4, 5 , 6]'''


