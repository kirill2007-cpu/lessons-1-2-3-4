from array import *

newArray = array('i', [3,1,2,2,2])
for i in range(len(newArray)):
  print(newArray[i])

arrayNumber = int(input('Enter a number from the array: '))
counter = newArray.count(arrayNumber)

print("Number", arrayNumber, "appears in the array", counter, "times")