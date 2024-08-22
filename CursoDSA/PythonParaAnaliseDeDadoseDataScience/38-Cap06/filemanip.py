import os
import csv
#print(os.getcwd())
#arq1 = open("/home/alexandre/CursosDSATeste/CursoDSA/PythonParaAnaliseDeDadoseDataScience/38-Cap06/arquivos/arquivo1.txt")
#print(arq1.read())
#arq1.close()

f = open('/home/alexandre/CursosDSATeste/CursoDSA/PythonParaAnaliseDeDadoseDataScience/38-Cap06/arquivos/salarios.csv', 'r')
#print(f.read())
xx=f.read()
rows=xx.split("\n")
#print(rows)
#print(type(rows))
#print(rows)

for row in rows:
    print(row.split(" "))