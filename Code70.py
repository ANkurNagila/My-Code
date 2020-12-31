x=int(input())
A=list(map(int,input().strip().split(" ")))[:x]

for i in range(1,x+1):
    if A[i-1]+i>x:
        print(i)
        break
