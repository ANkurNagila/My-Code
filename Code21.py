def Borderh(A,X,Y):
    maximum=0
    for i in range(X):
        line=0
        flag=None
        for j in range(Y):
            if A[i][j]=="#":
                if i==0:
                    line+=1
                    if line>maximum:
                        maximum=line
                elif i==X-1:
                    line+=1
                    if line>maximum:
                        maximum=line
                else:
                    if (A[i-1][j]=="#" and A[i+1][j]!="#"):
                        if flag==0 or flag==None:
                            line+=1
                            flag=0
                        else:
                            flag=None
                            line=0
                        if line>maximum:
                            maximum=line
                    elif (A[i-1][j]!="#" and A[i+1][j]=="#"):
                        if flag==-1 or flag==None:
                            line+=1
                            flag=-1
                        else:
                            line=0
                            flag=None
                        if line>maximum:
                            maximum=line
                    elif A[i-1][j]!="#" and A[i+1][j]!="#":
                        line+=1
                        if line>maximum:
                            maximum=line
                    else:
                        line=0
            else:
                line=0
    return maximum


def Borderv(A,X,Y):
    maximum=0
    for i in range(Y):
        flag=None
        line=0
        for j in range(X):
            if A[j][i]=="#":
                if i==0:
                    line+=1
                  
                    if line>maximum:
                        maximum=line
                elif i==Y-1:
                    line+=1
                 
                    if line>maximum:
                        maximum=line
                else:
                    if A[j][i-1]=="#" and A[j][i+1]!="#":
                        if flag==0 or flag==None:
                            line+=1
                            flag=0
                        else:
                            line=0
                            flag=None
                    elif A[j][i-1]!="#" and A[j][i+1]=="#":
                        if flag==-1 or flag==None:
                            line+=1
                            flag=-1
                        else:
                            line=0
                            flag==None
                        if line>maximum:
                            maximum=line
                    elif A[j][i-1]!="#" and A[j][i+1]=="#":
                        line+=1
                     
                        if line>maximum:
                            maximum=line
                    else:
                        line=0
            else:
                line=0
    return maximum






T=int(input())
A=[]
while T>0:
    X,Y=map(int,input().split(" "))

    for i in range(X):
        A.append(input())

    maximum1=Borderh(A,X,Y)
    maximum2=Borderv(A,X,Y)
    if maximum1>maximum2:
        maximum=maximum1
    else:
        maximum=maximum2
    print(maximum)
    A.clear()
    T-=1
