##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
with open('data.csv', 'r') as f:
    for linea in f.readlines():
        c = linea.split('\t')[3].replace(',','')
        d = linea.split('\t')[4] 
        l = d.split(',')
        b = [linea.split('\t')[0]]
        for i in b:
            print(i+','+str(len(c))+','+str(len(l)))
            
