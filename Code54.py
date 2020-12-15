def number(arr,all,counte):
    sum=0
    for i in arr:
        sum+=all[i]*(counte-all[i])
    return int(sum/2)

for i in range(int(input())):
    t=int(input())
    x=list(map(int,input().strip().split(" ")))[:t]

    even=[]
    odd=[]
    all={}
    counte=0
    counto=0

    for y in x:
        if y%2==0:
            if y not in even:
                even.append(y)
            counte+=1
        elif y%2!=0:
            if y not in odd:
                odd.append(y)
            counto+=1
        try:
            all[y]+=1
        except:
            all[y]=1

    #print(even,counte,odd,counto,all)
    sum=number(even,all,counte)+number(odd,all,counto)

    print(sum)
    print( )
