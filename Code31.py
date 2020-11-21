N=int(input())

T=list(map(int,input().split(" ")))[:N]
T.sort()
flag=0
prev=None
if max(T)-min(T)+1>N:
    print("NO")
else:
    for i in range(min(T),max(T)+1):
        if i in T:
            continue
        else:
            print("NO")
            flag=1
            break

    if flag==0:
        print("YES")
