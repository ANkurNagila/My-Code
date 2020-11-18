S,X,N=map(int,input().split(" "))
R=S
flag=1
prev=0
for x in range(N):
    day,km=map(int,input().split(" "))

    if (day-1-prev)*X>=R and flag!=0:
        count=prev+int(S/X)
        #print("count 1:",count,R)
        flag=0
    else:
        R=R-km-(day-1-prev)*km
        count=day
        prev=day
        #print("count 2:",count,R)

if flag==1:
    count=count+int(R/X)


print(count)
