
#A = list(map(int,input("").split(" ")))

A=[1,1,1,1,4,5,3,2,1,6,7]
A.sort()
#print(A)
new=0
x=0

for i in A:
    if i==x:
        new+=1
        #print(i,":\t",new)

    else:
        if new>=(len(A)//2):
            print(x)
        new=1
        #print(i,":\t",new)
        x=i
