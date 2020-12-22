S,P,T,H,x=map(int,input().strip().split(" "))
 
if P-x>=T:
    total=S*x
 
else:
    ticn=P-T
    tich=x-ticn
    total=tich*H+ticn*S
 
print(total)
