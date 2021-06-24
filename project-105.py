import math 
import csv
import statistics
from typing import Sized
with open("sd.csv", newline='')as f:
    csvReader=csv.reader(f)
    fileData=list(csvReader)
data=fileData[0]
squaredList=[]
for number in data:
    a=int(number)-statistics.mean(data)
    a=a**2
    squaredList.append=a
sum=0
for i in squaredList:
    sum=sum+i
result=sum/(len(data)-1)
sd=math.sqrt(result)
print (sd)