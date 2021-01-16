Test=input()
new=Test.split("&")
Res={}
count=0
lise=["username","pwd","profile","role","key"]
res=""
for x in new:
    #print(x)
    count+=1
    t=x.split("=")
    if (t[0] not in lise) and count!=1:
        count-=1
        if len(t)<2:
            res=res+"&"+t[0]
        else:
            res=res+"&"+x
    else:
        res=t[1]
    if count==1:
        Res["username"]=res
    elif count==2:
        Res["pwd"]=res
    elif count==3:
        Res["profile"]=res
    elif count==4:
        Res["role"]=res
    else:
        Res["key"]=res
    t.clear()

for i,j in Res.items():
    print(f"{i}: {j}")
