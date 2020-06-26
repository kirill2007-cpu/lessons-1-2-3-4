import os
import sys

path = os.getcwd()
# myname = "/newfilder"
compNameKebab = sys.argv[1]

print(compNameKebab)

try:
  os.mkdir(path + "/" + compNameKebab)
except OSError:
  print("Создать директорию не удалось")
else:
    print("Успешно создана директория")

f = open(path + "/" + compNameKebab +"/fil.txt","w")
f.write("gg")