##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.replace('\t','')for line in txt]
c = sorted(set([row[0]for row in txt]))
s = [[row[0],row[1]]for row in txt]
aa =0
for i in c:
    aa = [row[1] for row in s[:]if row[0]==i]
    maximo = max(aa)
    minimo = min(aa)
    print(i+','+maximo+','+minimo)
    
