t=[]

for i in range(3):
    t.append(input())

res=""
ver=[]
for i in range(3):
    ver.append(t[0][i]+t[1][i]+t[2][i])
line1=t[0]
line2=t[1]
line3=t[2]
line4=ver[0]
line5=ver[1]
line6=ver[2]
line7=t[0][0]+t[1][1]+t[2][2]
line8=t[0][2]+t[1][1]+t[2][0]

res=[]
res.append(line1)
res.append(line2)
res.append(line3)
res.append(line4)
res.append(line5)
res.append(line6)
res.append(line7)
res.append(line8)

X=res.count("XXX")
O=res.count("OOO")
x=0
o=0
dot=0

for i in t:
    x+=i.count("X")
    o+=i.count("O")
    dot+=i.count(".")

if x<o:
    print("Wait, what?")
elif x>=o and x-o<=1:
    if X>0 and O==0:
        if x<=o:
            print("Wait, what?")
        else:
            print("X won.")
    elif O>0 and X==0:
        if x>o:
            print("Wait, what?")
        else:
            print("O won.")
    elif X>0 and O>0:
        print("Wait, what?")
    elif (X==0 and O==0) and x==o and dot>0:
        print("X's turn.")
    elif (X==0 and O==0) and x>o and dot>0:
        print("O's turn.")
    elif X==0 and O==0 and dot==0:
        print("It's a draw.")
elif x>o and x-o>1:
    print("Wait, what?")
