import math

supp={}
supp[1]=0
for i in range(1,9):
    supp[5**i]=(supp[5**(i-1)]*5)+1

#print(supp)


Test=int(input())

while Test>0:
    Inp=int(input())
    y=0
    flag=1
    val=[]
    for j in range(8,0,-1):
        #print(5**j,":",end="\t")
        x=Inp//supp[5**j]
        #print(x)
        val.append(x)



        if j==1:
            y=(5**j)*x

        Inp=Inp-x

        if x!=0 and flag==1:
            z=Inp%supp[5**j]
            flag=0

    val.reverse()

    for i in range(2,8):
        t=int(y/(5**i))
        #print(t,val[i-1])

        if t!=val[i-1]:
            print("0")
            flag=2
            break


    if flag!=2:
        print("5")
        for i in range(5):
            print(y+i,end=" ")


    print()



    #print(y)


    Test-=1
