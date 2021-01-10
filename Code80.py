from pprint import pprint
file=open("D:\eext.txt")
file=file.read()

words=file.split(" ")
x=0
y=70
count=0
countl=0
result=[]
for i in range(1,len(words)//70+2):
    a=words[x:y]
    x=y
    y=(i+1)*70
    count+=70
    countl+=1
    t=" ".join(a)
    result.append(t)

if len(words)%70!=0:
    result.append(" ".join(words[x:]))
    l_1=1
else:
    l_1=0

for i in result:
    print(i)
print("Number of words:",count+len(words)%70)
print("Number of sentences:",countl+l_1)
