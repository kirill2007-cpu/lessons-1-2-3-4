# arr = input() 
# l = list(map(int,arr.split(' ')))
# l.reverse()
# print(l)


from array import *

newArray = array('i', [])
more = int(input('How many items: '))

for y in range(0,more):
  newValue = int(input('Enter num: '))
  newArray.append(newValue)

newArray.reverse()
print(newArray)