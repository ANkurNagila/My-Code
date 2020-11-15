x,k=map(int,input().split(" "))
x=str(x)
n=0

for i in x:
    i=int(i)
    if i<9 and k>0:
        n=n*10+9
        k-=1
    else:
        n=n*10+i

print(n)
