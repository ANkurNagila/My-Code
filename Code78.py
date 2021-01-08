for _ in range(int(input())):
    number,amount=map(int,input().split(" "))

    person=[]
    sum=0
    flag=0

    for i in range(number):
        person.append(int(input()))
        if flag==0:
            sum+=person[i]
            if sum==amount:
                flag=1
            elif sum>amount:
                c=0
                while sum>amount:
                    sum=sum-person[c]
                    c+=1
                if sum==amount:
                    flag=1


    if flag==0:
        print("NO")
    else:
        print("YES")

    person.clear()
