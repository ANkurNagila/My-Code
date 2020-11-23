test=int(input())
while t:
  n=int(input())
  temp1=len(bin(n)[2:])
  if bin(n)[2:].count('0')==0:
    print(n)
  else:
    print(int(2**(temp1-1))-1)
  t=t-1
