N=int(input())
mini=N+1
p=int(N**0.5)
for i in range(p,1,-1):
    if N%i==0:
        mini=i+N//i
        break
print(mini)
