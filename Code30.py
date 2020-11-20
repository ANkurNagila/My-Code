def multiples(N):
    t=[]
    c=N
    for x in range(2,N+1):
        if c%x==0:
            t.append(x)
            c=c/x
    #print("N:",N,"T:",t)
    return t

def removing_some_multiples(t):
    for x in t:
        j=multiples(x)
        for i in j:
            if i in t and i!=x:
                t.remove(i)

    return t



def lcm(D):
    #print(D)
    f={}
    result=1
    for x in D:
        x=int(x)
        #print(x)
        f[x]=multiples(x)
    common=list()
    for i in f.values():
        for j in i:
            if j not in common:
                common.append(j)


    removing_some_multiples(common)

    for k in common:
        result=result*k
    return result


D = input().split(" ")
print(lcm(D))
