N=int(input())

T=input()

Test=int(input())

for i in range(Test):
    res=""
    x,y=map(int,input().split(" "))
    p=T[:2*x-1]
    r=T[2*y-1:]
    #print(T[2*y-1:])

    q=T[2*x-2:2*y].replace("0","A")
    q=q.replace("1","B")
    q=q.replace("B","0")
    q=q.replace("A","1")

    if x!=1 and y!=N:
        res=p+q+r
        #print("1")

    elif x==1 and y!=N:
        res=q+r
        #print(q,r)
        #print("2")


    elif x!=1 and y==N:
        res=p+q
        #print("3")

    else:
        res=q
        #print("4")
    T=res
    print(T)

print(T)
