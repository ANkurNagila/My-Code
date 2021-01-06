Month=["January","February","March","April","May","June","July","August","September","October","November","December"]
x=28
Days=[31,x,31,30,31,30,31,31,30,31,30,31]
Res=""
for _ in range(int(input())):
    Test=input().split(" ")

    if (int(Test[2])%4==0 and int(Test[2])%100!=0) or (int(Test[2])%4==0 and int(Test[2])%100==0 and int(Test[2])%400==0):
        Days[1]=29
    else:
        Days[1]=28

    if Test[0]=="1":
        if Test[1]==Month[0]:
            Res="31 "+str(Month[11])+" "+str(int(Test[2])-1)
        
        else:
            Res=str(Days[Month.index(Test[1])-1])+" "+str(Month[Month.index(Test[1])-1])+" "+Test[2]
    
    else:
        Res=str(int(Test[0])-1)+" "+Test[1]+" "+Test[2]

    
    print(Res)
