N=int(input("Input no of Questions:"))
num=100/N
Number=0
Key=input("Enter Answer Key:")

for i in Key:
    t=0
    res=ord(i)-65 #ascii value of A
    Ans=input("Enter Answers As X & O:")
    count=0
    for j in Ans:
        if (ord(j)-88+t)==res: #Ascii value of X
            count+=1
        t+=1
    if count==1:
        Number+=num
print(Number)
