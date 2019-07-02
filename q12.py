##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.replace('\t',',')for line in txt]
txt = [line.split(',')for line in txt]
m = [[row for row in line if len(row) == 1] for line in txt]
m = [line[1:] for line in m]
a = [line[2:] for line in m]
b = []
for i in a:
    for j in i:
        b = b+[j]
b = set(b)
b = list(b)
b = sorted(b)

d = []
for i in b:
    n = [i]
    c = 0
    for row in m:
        if i in row:
            c = c+int(row[0])
    n = n+[c]
    d = d+[n]
for i in d:
    u = i[0]+","+str(i[1])
    print(u)
