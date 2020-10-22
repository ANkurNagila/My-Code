Take=input("Enter the value to find if it is Armstrong number: ")

n=len(Take)
Take=int(Take)
f=0
Take1=Take

for N in range(1,n+1):
    t=Take1%10
    Take1=int(Take1/10)
    f=f+t**n

if Take==f:
    print("Yes it is Armstrong number: "+ str(f))

else:
    print("No it is not a Armstrong number")
