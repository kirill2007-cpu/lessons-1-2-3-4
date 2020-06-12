from array import *

givenArray = array('i', [7, 3, 12, 1, 8])

while True:
  selectedValue = int(input('Select one of a number from the array: '))
  
  if(selectedValue in givenArray):
    print(givenArray.index(selectedValue))
    break
  else:
    print("Try again")