import csv
import os
import sys

##print(sys.path[0])
##print(os.getcwd())
#print(os.path.abspath(sys.argv[0]))
#print(os.path.join(os.getcwd() + "CursoDSA/PythonParaAnaliseDeDadoseDataScience/38-Cap06/arquivos/salarios.csv"))

##arquivo = open(os.path.join(os.getcwd() + "/arquivos/salarios.csv"),"r")
##with arquivo :
##    print(csv.DictReader(arquivo.read()))
##    print("1")
##    abc = csv.
#print(os.path.join(os.path.abspath())
#f = csv.reader("")

import os
import sys
arquivo = open(os.path.join(os.getcwd() + "/CursoDSA/PythonParaAnaliseDeDadoseDataScience/38-Cap06/arquivos/salarios.csv"),"r")

import csv
import pprint
reader = csv.reader(arquivo)
##print(next(reader))
##print(next(reader))
##print(next(reader))
lista = list(reader)
print("--")
pprint.pprint(lista)
arquivo.close