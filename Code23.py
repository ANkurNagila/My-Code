T=int(input())

A=[]
a=[]

for t in range(65,91,2):
    flag=1
    for i in range(2, int(t**1/2)):
         if t % i == 0:
             flag=0
    if flag!=0:
        A.append(t)

for t in range(97,123,2):
    flag=1
    for i in range(2, int(t**1/2)):
         if t % i == 0:
             flag=0
    if flag!=0:
        a.append(t)


res=[]
retake={}

while T>0:
    N=int(input())

    S=input()

    for i in S:
        x=ord(i)
        if i in retake.keys():
            print(retake[i],end="")
        elif x<=93:
            for j in A:
                q=x-j
                if q<0:
                    q=-1*q
                res.append(q)
            y=chr(A[res.index(min(res))])
            print(y,end="")
            retake[i]=y
            res.clear()

        else:
            for j in a:
                q=x-j
                if q<0:
                    q=-1*q
                res.append(q)
            y=chr(a[res.index(min(res))])
            print(y,end="")
            retake[i]=y
            res.clear()
    print()
    T-=1
