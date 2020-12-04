def check(c1,c2,city_d,K):
    sum=city_d[c1]-city_d[c2]
    if sum<0:
        sum*=-1
    if sum>K//2:
        print(K-sum)
    else:
        print(sum)


N,K=map(int,input().strip().split(" "))
city_d={}
for j in range(K):
    s1=input().split()
    for i in s1[1:]:
        city_d[i]=j+1
#print(city_d)

Q=int(input())

for i in range(Q):
    c1,c2=map(str,input().strip().split(" "))
    check(c1,c2,city_d,K)
