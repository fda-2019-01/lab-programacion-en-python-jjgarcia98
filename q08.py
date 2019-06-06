##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.replace('\t','')for line in txt]
c = sorted(set([row[1]for row in txt]))
s = [[row[0],row[1]]for row in txt]
aa =0
a = ()
for i in c:
    aa = sorted([row[0] for row in s[:]if row[1]==i])
    a = (str(i),(aa))
    print(a)
    
