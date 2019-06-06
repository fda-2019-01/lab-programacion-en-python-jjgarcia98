##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
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
    aa = ([row[0] for row in s[:]if row[1]==i])
    a = (str(i),(aa))
    print(a)
    
