t=[]

for _ in range(int(input())):
    for i in range(4):
        t.append(input())

    res=""
    ver=[]
    flag=0
    for i in range(4):
        ver.append(t[0][i]+t[1][i]+t[2][i]+t[3][i])
    line1=t[0]
    line2=t[1]
    line3=t[2]
    line4=t[3]
    line5=ver[0]
    line6=ver[1]
    line7=ver[2]
    line8=ver[3]
    line9=t[0][0]+t[1][1]+t[2][2]
    line10=t[0][2]+t[1][1]+t[2][0]
    line11=t[0][1]+t[1][2]+t[2][3]
    line12=t[0][3]+t[1][2]+t[2][1]
    line13=t[1][0]+t[2][1]+t[3][2]
    line14=t[1][2]+t[2][1]+t[3][0]
    line15=t[1][1]+t[2][2]+t[3][3]
    line16=t[1][3]+t[2][2]+t[3][1]

    res=[]
    res.append(line1)
    res.append(line2)
    res.append(line3)
    res.append(line4)
    res.append(line5)
    res.append(line6)
    res.append(line7)
    res.append(line8)
    res.append(line9)
    res.append(line10)
    res.append(line11)
    res.append(line12)
    res.append(line13)
    res.append(line14)
    res.append(line15)
    res.append(line16)


    find=["xx..",".x.x",".xx.","..xx","oxx.",".xxo","o.xx","xx.o","ox.x","x.xo","x.x.","x.xx","xx.x","x.x","xx.",".xx"]
    for i in find:
        if i in res:
            print("YES")
            flag=1
            break
    if flag==0:
        print("NO")

    res.clear()
    t.clear()
