##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
txt = open('data.csv','r').readlines()
txt = [row[0:-1]for row in txt]
txt = [line.replace('\t','')for line in txt]
c = sorted(set([row[7]+row[8]for row in txt]))
s = [row[7]+row[8]for row in txt]
aa =0
for i in c:
    aa = s.count(i)
    print(i+','+str(aa))
    
