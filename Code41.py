N,R,C=map(int,input().split(" "))

A=[]

for i in range(N):
    B=list(map(int,input().strip().split(" ")))
    A.append(B)

x=list(map(int,input().strip().split(" ")))[:R]
y=list(map(int,input().strip().split(" ")))[:C]

for i in x:
    #print("\n",A[i-1])
    A[i-1]= A[i-1][-1:] + A[i-1][:-1]
    #print(A[i-1])
#print(A)
for j in y:
    for i in range(N,0,-1):
        if i==N:
            t=A[i-1][j-1]
            A[i-1][j-1]=A[i-2][j-1]
        elif i==1:
            A[i-1][j-1]=t
        else:
            A[i-1][j-1]=A[i-2][j-1]

    #print(j,":\t",A)

for i in range(N):
    for j in range(N):
        print(A[i][j],end=" ")
    print()
#print(A)
