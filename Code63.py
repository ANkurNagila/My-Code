for _ in range(int(input())):
    int(input())
    array = list(map(int, input().split()))
    sum_ = 0
    for i in array:
        sum_+=i&(-i)
    print(sum_)
