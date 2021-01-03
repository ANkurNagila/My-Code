x=input()
t=[]
s=0
for i in x:
    if i in t:
        s+=1
    else:
        t.append(i)

print(s)
