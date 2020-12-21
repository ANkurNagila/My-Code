x,y=map(int,input("Enter two numbers to find greatest common divisior:").split(" "))

if y>x:
    x,y=y,x

while y!=0:
    t=y
    y=x%y
    x=t

print("Greatest common Divisior:",x)
