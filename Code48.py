t=input()

try:
    t=int(t)
    print("Invalid Input")
except:
    res=""
    i=True
    for x in t:
        if x=="G":
            res+="C"
        elif x=="C":
            res+="G"
        elif x=="T":
            res+="A"
        elif x=="A":
            res+="U"
        else:
            print("Invalid Input")
            i=False
            break

    if i==True:
        print(res)
