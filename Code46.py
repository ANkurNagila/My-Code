for i in range(int(input())):
    s = input()
    s1 = s[0].lower()
    for c in s[1:]:
        if ord(c) < 97:
            s1 += '_'+c.lower()
            continue
        s1 += c
    print(s1)
