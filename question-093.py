from array import *

inputArray = array('i', [])
newArray = array('i', [])

print('Enter five numbers: ')


for y in range(0,5):
  newValue = int(input('Enter num: '))
  inputArray.append(newValue)
sortedResult = sorted(inputArray)

for i in range(len(sortedResult)):
  print(sortedResult[i])

# print("Select one of a number from the array: ")
selectedValue = int(input('Select one of a number from the array: '))
sortedResult.remove(selectedValue)
newArray.append(selectedValue)

#test output
print(sortedResult)
print(newArray)
