from array import *

givenArray = array('i', [21, 99, 34, 67, 11])

while True:
  inputNumber = int(input('Enter a number between 2 and 5: '))
  if inputNumber >=2 and inputNumber<=5:
    break
  else:
    print("Try again!!!")

for i in range(len(givenArray)):
  divided = givenArray[i]/inputNumber
  print(round(divided, 2))