for i in range(int(input())):
    x,y=map(int,input().split(" "))
    flag=1
    while x!=0:
        if x%y==1 or x%y==0:
            x=x//y
        else:
            flag=0
            break

    if flag==1:
        print("YES")
    else:
        print("NO")
