N,Q=map(int,input().split(" "))

A=list(map(int,input().split(" ")))

while Q>0:
    
    L,R=map(int,input().split(" "))
    sum=0
    for i in range(L-1,int(R/2)+1):
        sum=sum+A[i]+A[R-i]
        #print(sum)

    if (R-L)%2==0:
        sum=sum-A[int((L+R)/2)-1]
    mean=sum/(R-L+1)

    print(int(mean))
    Q-=1
