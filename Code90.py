for _ in range(int(input())):
    x,y,l,m,a,b=map(int,input().split(" "))

    p=x-a
    q=y-b

    if l<=p and m<=b:
        print("bottom-right")
    elif l<=a and m<=b:
        print("bottom-left")
    elif l<=p and m<=q:
        print("top-right")
    else:
        print("top-left")
