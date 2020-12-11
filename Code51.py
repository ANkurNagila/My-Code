Test=int(input())

while Test>0:
    N=int(input())


    sum1=0
    sum2=0
    Bob = list(map(int,input().strip().split(" ")))[:N]
    Alice = list(map(int,input().strip().split(" ")))[:N]
    sum1=max(Bob)
    sum2=max(Alice)

    if sum1>sum2:
       print("Bob")
    elif sum2>sum1:
        print("Alice")
    else:
        print("Tie")

    Test-=1
