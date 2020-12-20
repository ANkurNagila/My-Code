for j in range(int(input())):
    N=int(input())
 
    input1=input()
    input2=input()
 
 
    count=0
    flag=0
    for i in range(N):
        if input1[i]!=input2[i]:
            if (input2.count(input1[i])==0 and (input1.count(input1[i]))%2!=0) or (input1.count(input2[i])==0 and (input2.count(input2[i]))%2!=0):
                print("NO")
                flag=1
                break
            count+=1
            if count>3:
                print("NO")
                flag=1
                break
 
    if flag==0:
        print("YES")
