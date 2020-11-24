t="h a c k e r t"
tres=t.split()

r={}

for x in tres:
    r[x]=0


N=int(input())

test=input()

for i in test:
    if i in tres:
        if i=="e" or i=="a" or i=="r" or i=="h":
                r[i]+=0.5
        else:
                r[i]+=1

for i in r.keys():
        r[i]=int(r[i])


print(min(r.values()))
