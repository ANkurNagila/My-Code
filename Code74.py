for i in range(int(input())):
    Test=input()
    x=1
    flag=0
    for i in range(len(Test)):
        x=x*(ord(Test[i])-96)
            #print(str(ord(Test[i])-96),end=" ")

        if Test[i]==Test[-i-1] and flag==0:
            pass
        else:
            flag=1
    if flag==1:
        print(x)
    else:
        print("Palindrome")
