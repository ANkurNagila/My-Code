for i in range(int(input())):
    t=int(input())
    x=list(map(int,input().strip().split(" ")))[:t]

    des={}
    flag=1
    num=0
    for i in x:
        if i>t:
            flag=0
        try:
            des[i]+=1
        except:
            des[i]=1


    for i,j in des.items():
        if j<i:
            flag=0
            break
        elif j%i==0:
            num=num+int(j/i)
        elif j%i!=0:
            flag=0
            break

    if flag==1:
        print(num)
    else:
        print("Invalid Data")
