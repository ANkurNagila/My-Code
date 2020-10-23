N=int(input("Enter N to form fibonacci series:"))

series=0
i=0
a=0
t=1

print(a)
print(t)
while i<N:
    series=a+t
    print(series)
    a=t
    t=series
    i=i+1;
