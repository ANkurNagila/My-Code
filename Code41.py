from collections import Counter

N,R,C=map(int,input().split(" "))

A=[]

for i in range(N):
    A.append(list(map(int,input().split())))

x=Counter(list(map(int,input().split())))
y=Counter(list(map(int,input().split())))

for i in x:
    #print("\n",A[i-1])
    A[i-1]= A[i-1][-x[i]:] + A[i-1][:-x[i]]
    #print(A[i-1])
#print(A)

A=list(map(list,zip(*[i for i in A])))

for j in y:
    A[j-1]= A[j-1][-y[j]:] + A[j-1][:-y[j]]

A=list(map(list,zip(*[i for i in A])))


for i in range(N):
    print(' '.join(map(str,A[i])))
