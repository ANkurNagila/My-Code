for i in range(int(input())):
    n=int(input())

    p=(n-1)//3
    q=(n-1)//5
    r=(n-1)//15
    sum=((p)*(3+3*(p))+((q*(5+5*(q))-((r*(15+15*(r)))))))//2
    print(sum)

    
