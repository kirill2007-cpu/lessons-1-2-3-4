import random
from array import *

newArray = array('i', [])

print("Enter three numbers")

for _ in range(0,3):
  newValue = int(input('Enter num: '))
  newArray.append(newValue)

randomArray = array('i', [])

for _ in range(5):
  randomArray.append(random.randint(1,10))

newArray.extend(randomArray)
sortedResult = sorted(newArray)

for i in range(len(sortedResult)):
  print(sortedResult[i])