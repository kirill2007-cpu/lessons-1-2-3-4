import sys
import os

path = os.getcwd()
str = sys.argv[1]
# print(cmpntName[2:])

# str = "hello-my-sun"
# print(str.split("-"))
res =[]
for w in str.split("-"):
    res.append(w.capitalize())
print(res)
print("".join(res))