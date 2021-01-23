K=int(input())
Test=input()

res=[]

for i in range(len(K)):
    try:
        t=Test[i:i+K]
        if t not in res:
            res.append(t)
    except:
        continue

print(count(res))
