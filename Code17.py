def line(max):
    for i in max:
        print("+-",end="")
        for j in range(i):
            print("-",end="")
        print("-",end="")
    print("+")


T=int(input())
while(T>0):
    Row,Column=map(int,input().split(" "))
    data={}
    maxi=[]
    for i in range(Row):
        maxi.append(0)

    for i in range(0,Column+1):
        Attr=list(map(str,input().strip().split(" ")))[:Row]
        #print(Attr)
        data[i]=Attr
        for j in range(Row):
            if len(Attr[j])>maxi[j]:
                maxi[j]=len(Attr[j])

    line(maxi)
    x=" "
    for i in data.values():
        #print(i)
        count=0

        if data[0]==i:
            for j in i:
                l=len(j)
                j=j+" "*(maxi[count]-len(j))
                x=x+j+" | "
                count+=1
            print("|"+x)
            x=" "
            line(maxi)

        else:
            for j in i:
                try:
                    les=int(j)
                    l=len(j)
                    #print("\t\t",j)
                    j=" "*(maxi[count]-len(j))+j
                    count+=1
                except:
                    l=len(j)
                    j=j+" "*(maxi[count]-len(j))
                    count+=1
                x=x+j+" | "
            print("|"+x)
            x=" "

    line(maxi)
    T-=1
