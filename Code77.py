Test=input()
flag=1
if ("l" in Test) and ("o" in Test) and ("v" in Test) and ("e" in Test):
    try:
        p=Test.index("l")
    except:
        print("Let us breakup!")
        flag=0

    if flag==1:
        Test1=Test[p+1:]
        try:
            q=Test1.index("o")
        except:
            print("Let us breakup!")
            flag=0

    if flag==1:
        Test2=Test1[q+1:]
        try:
            r=Test2.index("v")
        except:
            print("Let us breakup!")
            flag=0

    if flag==1:
        Test3=Test2[r+1:]
        try:
            s=Test2.index("e")
        except:
            print("Let us breakup!")
            flag=0


    if flag==1:
        print("I love you, too!")
else:
    print("Let us breakup!")
