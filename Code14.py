import statistics

N,Q=map(int,input().split(" "))

Whole=list(map(int,input().split(" ")))
while Q>0:                                                                    ##Time Limit error
    L,R=map(int,input().split(" "))

    print(int(statistics.mean(Whole[L-1:R])))
    Q-=1


    
    
    
        ################################################################################################################################# 
m, n = map(int, input().split())
a = list(map(int, input().split()))
s = []
s1 = 0
for i in range(m):
    s1 += a[i]
    s.append(s1)                                                                ##Correct Method
for i in range(n):
    x, y = map(int, input().split())
    if x == 1:
        print((s[y-1])//(y-x+1))
    else:
        print((s[y-1] - s[x-2])//(y-x+1))
        
        #######################################################################################################################################
