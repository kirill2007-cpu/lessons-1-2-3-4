from array import *

newArray = array('i', [])
while True:
  if len(newArray) >= 5:
    break
  number = int(input('Enter a number: '))
  if number >=10 and number<=20:
    newArray.append(number)
  else:
    print("Outside the range")
    continue
  
print("Thank you")
for i in range(len(newArray)):
  print(newArray[i])