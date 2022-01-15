import csv
import math

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    data=list(reader)

data1=data[0]

def mean(data1):
    n=len(data1)
    total=0

    for x in data1:
        total=total+int(x)
    mean=total/n
    return mean 
squarelist=[]
for f in data1:
    a=int(f)-mean(data1)
    a=a**2
    squarelist.append(a)
sum=0
for d in squarelist:
    sum=sum+d
result=sum/(len(data1)-1)   
standardduration=math.sqrt(result)
print(standardduration)
