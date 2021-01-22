for _ in range(int(input())):
    n,m=map(int,input().split())
    s=0
    while(n>0):
        s+=((n+1)//2)**2
        n//=2

    print(s%m)
