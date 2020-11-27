def Fib(N):
    if N<=1:
        return N
    for i in range(2,N+1):
        result=Fib(i-1)+Fib(i-2)
    return result

N=int(input())

Last=(Fib(N))%10
print(Last)
