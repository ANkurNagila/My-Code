i=input()

if i[0]==i[len(i)-1] and len(i)>1 and i.count(i[0])!=len(i):
    print(len(i)-1)
elif len(i)<=1 or i.count(i[0])==len(i):
    print("0")
else:
    print(len(i))
