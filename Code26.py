t=int(input())



while t>0:
    l,r,s=map(int,input().split(" "))
    
    
    if s>r  or r<l:
        print("-1 -1")
    
    
    
    else:
        if (l<=s or l%s==0) and int(l//s)!=0:
            x=int(l//s)
        else:
            x=int(l//s)+1
        y=int(r//s)

        if x>y:
            print("-1 -1")
        else:
            print(x,y)


    t-=1
