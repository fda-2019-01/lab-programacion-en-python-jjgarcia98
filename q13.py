##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
with open('data.csv', 'r') as f:
    for linea in f.readlines():
        d = linea.split('\t')[4] .replace('\n','')
        b = [linea.split('\t')[0]]
        a=("".join([x for x in d if x.isdigit()]))
        x=0
        for i in a:
            x = x+int(i)
        for i in b:
            print(i+','+str(x))
            
