N=int(input())
A=[int(n) for n in input().split()]
Sum=[]
New=[]
Sum1=[]
j=1
T=0
s=0
New.append(0)
while T<N:
    T=T+j
    New.append(T)
    j+=1

for j in range(N):
    s=s+A[j]
    Sum1.append(s)

New.reverse()
j=0
#print(New)

#print(Sum1)
for i in range(N):
    s=0
    t=i

    try:
        if N-i>=New[j] and i!=0:
            s=Sum1[i+New[j]-1]-Sum1[i-1]
            Sum.append(s)
        elif i==0:
            s=Sum1[i+New[j]-1]
            Sum.append(s)
        else:
            j+=1
            if N-i>=New[j]:
               s=Sum1[i+New[j]-1]-Sum1[i-1]
               Sum.append(s)
    except:
        continue



#print(Sum)
x=max(Sum)
print(x)
