import sys
import os

path = os.getcwd()
compNameKebab = sys.argv[1]
dir_path = path + "/" + compNameKebab
indexjs_path = dir_path + "/index.js"
comptjs_path = dir_path + "/" + compNameKebab + ".js"
comptscss_path = dir_path + "/" + compNameKebab + ".scss"

def fromKebabToCamel(kebab):
  res = []
  for word in kebab.split("-"):
    res.append(word.capitalize())
  return "".join(res)

try:
  os.mkdir(dir_path)
except OSError:
  print("Directory creation failed")
else:
  print("Component have been created")

indexjs = open(indexjs_path, "w")
comptjs = open(comptjs_path, "w")
comptscss = open(comptscss_path, "w")

compNameCamel = fromKebabToCamel(compNameKebab)

indexjs.write("import " + compNameCamel + " from "+"\"./" + compNameKebab + "\"\n")
indexjs.write("export default " + compNameCamel)

comptjs.write("import React, { Component } from 'react'\n")
comptjs.write("import " + "\"./" + compNameKebab + "\"\n")
comptjs.write("export default class " + compNameCamel + " extends Component {\n")
comptjs.write("\trender() {\n")
comptjs.write("\t\treturn ()\n")
comptjs.write("\t}\n")
comptjs.write("}")

indexjs.close()
comptjs.close()
comptscss.close()
