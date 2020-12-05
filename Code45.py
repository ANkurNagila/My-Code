def taking_elements(lis1,N):
    for x in range(N):
        t=int(input())
        lis1.append(t)

def sort(lis1):
    lis2=list()
    count=1
    mini=None
    maxi=None
    while count<=len(lis1):
        if mini==None or lis1[count-1]<mini :
            lis2.insert(0,lis1[count-1])
            if mini==None:
                maxi=lis1[count-1]
            mini=lis1[count-1]
        elif maxi==None or lis1[count-1]>maxi:
            lis2.append(lis1[count-1])
            maxi=lis1[count-1]
        else:
            for x in range(0,count-1):
                if lis2[x]>lis1[count-1]:
                    lis2.insert(x,lis1[count-1])
                    break
        count+=1
    return lis2

N=int(input("Enter the number of elements in list:"))
print("We will take elements of list:")
first=list()
taking_elements(first,N)
print("Actual list:",first)
print("Sorted list:",sort(first))
