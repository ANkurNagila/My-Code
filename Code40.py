N,Z=map(int,input().split(" "))

def digitsum(x):
    total=0
    for letter in str(x):
        total+=int(letter)
    return total

fact=1
for i in range(1,N+1):
    fact=fact*i
x=str(fact)
while fact>10:
    fact=digitsum(fact)

print(len(x)+fact)
