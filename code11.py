
A = list(map(int,input("").split(" ")))

A.sort()
new=0
x=0

for i in A:
    if i==x:
        new+=1
        if new>=(len(A)//2):
            print(x)
        
    else:
        
        new=1
        x=i
