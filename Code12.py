T=int(input())

while T>0:
    res=0
    t1=[]
    t2=[]
    A = list(map(str,input("").split(" ")))
    x=A[0]
    y=A[1]
    res=1
    for i in x:
        t1.append(i)
    #    print("T1:",t1)
    for j in y:
        if j in t1:
            t1.remove(j)
    #        print("T1:",t1)
        else:
            res=0
            print("NO")
            break
    #        print("T2:",t2)
    if res==1:
        print("YES")
    T-=1
