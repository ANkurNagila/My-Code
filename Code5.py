Test=int(input())
f=dict()
T=2

while Test>0:
    Rate1,Rate2=map(int,input().split(" "))
    Final=0
    f["a"]=0
    f["b"]=0

    num=int(input())
    for x in range(num):
        a,b=map(int,input().split(" "))
        f["a"]=a+f["a"]
        f["b"]=b+f["b"]

    if T%2==0:
        Final=f["a"]*Rate1+f["b"]*Rate2
        T+=1
    else:
        Final=f["b"]*Rate1+f["a"]*Rate2
        T-=1


    print(Final,f)

    Test=Test-1
