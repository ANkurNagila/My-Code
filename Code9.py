t=int(input())
 
A = list(map(str,input("").split(" ")))
y=0
res=0
for x in A:
    if y<t/2:
        res=res*10+int(x[0])
    else:
        res=res*10+int(x[-1])
    y+=1
if(res%11==0):
    print("OUI")
else:
    print("NON")
