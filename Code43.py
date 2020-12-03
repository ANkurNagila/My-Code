def divide(dividend, divisor):
    sign = (-1 if((dividend < 0)^(divisor < 0)) else 1)
    quotient = 0
    temp = 0
    x=len(bin(dividend))-2
    for i in range(x, -1, -1):
        #print(i,":",end="  ")
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            #print(temp,end="  ")
            quotient |= 1 << i
            #print(quotient)
        #print()

    return sign * quotient



#divide(10,3)
T=[]
N=int(input())
for i in range(2,N+1):
    count=0
    for j in range(2,int(i**1/2)+1):
        if i-j*divide(i,j)==0:
            count+=1
    if count==0:
        T.append(i)

print(T)
