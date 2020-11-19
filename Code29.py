Test=int(input())

while Test>0:
    N=int(input())
    Arr=list(map(int, input().split()))[:N]
    x=0
    for i in range(N):
        x=x^Arr[i]
    maxi=x
    z=0
    y=0
    for i in range(N):
        y^=Arr[i]

        z=y & (y^x)

        if z>maxi:
            maxi=z
    print(maxi)
    Test-=1
