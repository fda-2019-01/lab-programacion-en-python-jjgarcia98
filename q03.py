##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
m = open('data.csv','r').readlines()
b=[row[2]for row in m]
a=([row[0]for row in m])
x=0
y=0
z=0
s=0
c=0
d=0
for i in a:
    if i == 'A':
        y = y + int(b[x])
    if i == 'B':
        z = z + int(b[x])
    if i == 'C':
        s = s + int(b[x])
    if i == 'D':
        c = c + int(b[x])
    if i == 'E':
        d = d + int(b[x])                            
    x=x+1
print('A'+','+str(y))
print('B'+','+str(z))
print('C'+','+str(s))
print('D'+','+str(c))
print('E'+','+str(d))
