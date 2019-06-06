##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.split('\t')for line in txt]
s = [row[-1]for row in txt]
s = [line.split(',')for line in s]
a = []
b = []
for i in s:
    for j in i:
        a.append(j)
        
a = [line.split(':')for line in a]
for i in a:
    for j in i:
        b.append(j)
d=[]
for i in b:
    if len(i) == 3:
        d.append(i)
x = sorted(set(d))
for i in x:
    aa = d.count(i)
    print(i+','+str(aa))
    
