import random
from array import *

newArray = array('i', [])

for _ in range(5):
  newArray.append(random.randint(1,10))

for i in range(len(newArray)):
  print(newArray[i])
