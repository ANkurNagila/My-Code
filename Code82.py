for _ in range(int(input())):
    N,Q=map(int,input().split(" "))

    houses=input()

    for i in range(Q):
        x,y=map(int,input().split(" "))

        if x<y and y!=N:
            case1=houses[x-1:y]
            case2=houses[y-1:]+houses[:x]
            #print("1")

        elif x>y and y!=N:
            case1=houses[y-1:x]
            case2=houses[x-1:]+houses[:y]
            #print("2")

        elif x<y and y==N:
            case1=houses[x-1:]
            case2=houses[N-1]+houses[:x]
            #print("3")

        elif x>y and x==N:
            case1=houses[y-1:]
            case2=houses[N-1]+houses[:y]
            #print("4")

        elif x<y and x==1:
            case1=houses[:y]
            case2=houses[y-1:]+houses[0]
            #print("5")

        elif x>y and y==1:
            case1=houses[:x]
            case2=houses[x-1:]+houses[0]
            #print("6")

        elif (x==1 and y==N) or (y==1 and x==N):
            case1=houses
            case2=houses[N-1]+houses[0]

        elif x==y:
            print(0)
            continue

        x1=case1.count("GR")+case1.count("RG")
        y1=case2.count("GR")+case2.count("RG")

        #print(case1,case2)

        if x1>=y1:
            print(y1)
        else:
            print(x1)
