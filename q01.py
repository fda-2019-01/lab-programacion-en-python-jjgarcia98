##
## Imprima la suma de la segunda columna.
##
m = open('data.csv','r').readlines()
a=[row[2]for row in m]
x=0
for i in a:
    x = x+int(i)
print(x)
