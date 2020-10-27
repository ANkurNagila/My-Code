def Opposite(N):
    if N%6==N%12 and N%6!=0:
        x=N%6
        y=2*(6-x)+1
        return N+y

    elif N%6==0:
        x=N%6
        if N%6==0 and N%12==0:
            y=-(2*(6-x-1)+1)
            return N+y
        else:
            return N+1

    else:
        x=N%6
        y=-(2*(x)-1);
        return N+y

def postion(N):
    if N%6==1 or N%6==0:
        return "WS"
    elif N%6==2 or N%6==5:
        return "MS"
    else:
        return "AS"



Test=int(input())
while Test>0:
    Seat_Number=int(input())
    print(Opposite(Seat_Number),postion(Seat_Number))
    Test-=1
