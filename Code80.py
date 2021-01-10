import re
from pprint import pprint
file=open("D:\eext.txt")
line2=""
result=[]
line2=""
for line in file:
    line2=line2+line
    x=re.findall(r"(\S+\s){70}",line2)

    for i in x:
        for count==0:
            res1=line2.index(i)
        i=i.strip()
        result.append(line2[:])
        line2=line2[line2.index(i)+1:]
pprint(result)

for i in result:
    x=i.split(" ")
    print(len(x))

print(result[2])
