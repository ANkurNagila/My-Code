N=int(input())
Array=list(map(int,input().strip().split(" ")))[:N]
sum=0
for i in range(1,N):
    if Array[i-1]>=Array[i]:
        x=Array[i-1]-Array[i]
        Array[i]=Array[i]+x+1
        sum+=x+1
print(sum)
