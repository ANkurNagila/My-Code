T=int(input())

A=list(map(int,input().split(" ")))

t=[]
for i in A:
    t.append(i%7)

sum=0

for j in t:
    sum=sum+j

f=sum%7
mn=None
min_pos=-1

for j in range(T):
    if t[j]==f:
        try:
            if A[j]<mn:
                mn=A[j]
                min_pos=j
        except:
            if mn==None:
                mn=A[j]
                min_pos=j

print(min_pos)
