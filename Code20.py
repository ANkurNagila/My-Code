def rec(a,b,c):
    if a>=b:
        return ((a-b)//2+(a-b)%2)
    if b%c==0:
        return (1+rec(a,b//c,c))
    else:
        x=(b//c+1)*c
        return ((x-b)//2+(x-b)%2+rec(a,x,c))




Test=int(input())

while Test>0:
    K,M,N=map(int,input().split(" "))
    print(rec(K,M,N));
    Test-=1
