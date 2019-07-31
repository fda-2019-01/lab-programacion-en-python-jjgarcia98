##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import glob
f=glob.glob("data.csv")
a = open("data.csv", "r").readlines()
a = [linea[:-1] for linea in a]
a = [linea.replace("\t", ",") for linea in a]
a = [linea.split(",") for linea in a]
a = [linea[5:] for linea in a]
c=[]
for linea in a:
  d = []
  for x in linea:
    if len(x)==5:
      d.append(x)
  c.append(d)
n = []
for i in c:
  for j in i:
    n.append(j)
n = sorted(n)
m = []
p=[linea.replace(":",",") for linea in n]
p=[linea.split(",") for linea in p]
s = set([linea[0]for linea in p])
z = []
for x in s:
  let=[x]
  for u in p:
    if u[0]==x:
      let.append(u[1])
  z= z+[let]
a1= []
for y in z:
  a2 = [y[0], min(y), max(y[1:])]
  a1= a1 + [a2]
a1 = sorted(a1) 
for e in a1:
  l= e[0]+","+e[1]+","+e[2]
  print(l)
    
