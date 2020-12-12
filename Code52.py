f=input()
count=dict()
for j in ["L","R","D","U"]:
    count[j]=0
for i in f:
    count[i]+=1

x=count["R"]-count["L"]
y=count["U"]-count["D"]
print(x,y)
