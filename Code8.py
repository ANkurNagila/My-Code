import re
N=int(input())

s=input()
s=s.upper()
t=""

for x in range(N):
    if s[x]==".":
        t+="B"
    else:
        t+=s[x]

if re.search("(HH)+",t):
    print("NO")
else:
    print("YES")
    print(t)
