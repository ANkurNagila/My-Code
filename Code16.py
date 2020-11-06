t=input()
y=None
flag=1
vowels=["A","E","I","O","U","Y"]
for i in t:
    try:
        x=int(i)
        if y!=None:
            z=y+x
            if z%2!=0:
                print("invalid")
                flag=0
                break
        y=x
       # print("int:",x)
    except:
        if i in vowels:
            print("invalid")
            flag=0
            break
        y=None

if flag==1:
    print("valid")
