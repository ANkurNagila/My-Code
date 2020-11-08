Test=int(input())

while Test>0:
    A,B,C=map(int,input().split(" "))

    if (A+C)%2==0:
        d=int((A+C)/2)
        count=d-B
        if count<0:
            count=-1*count
    
    else:
        d=int((A+C-1)/2)
        count=d-B
        if count<0:
            count=(-1)*count
        else:
            count=d-B+1


    print(count)
    Test-=1
        
