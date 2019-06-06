##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.replace('\t','')for line in txt]
c = sorted(set([row[0]for row in txt]))
s = [row[0]for row in txt]
aa =0
for i in c:
    aa = s.count(i)
    print(i+','+str(aa))
    
