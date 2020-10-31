T=int(input())

while T>0:
    res=0
    t1=[]
    t2=[]
    x=input()
    y=input()
    res=0
    for i in x:
        t1.append(i)
    #    print("T1:",t1)
    for j in y:
        if j in t1:
            t1.remove(j)
    #        print("T1:",t1)
        else:
            t2.append(j)
    #        print("T2:",t2)
    print(len(t1)+len(t2))
    T-=1
