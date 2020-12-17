for Test in range(int(input())):
    new=""
    word=input()
    Q=int(input())
    for i in word:
        if i in ["a","e","i","o","u"] and Q>0:
            a=chr(ord(i)+1)
            Q-=1
        else:
            a=i

        new=new+a

    print(new)
