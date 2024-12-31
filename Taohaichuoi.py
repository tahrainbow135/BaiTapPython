t = int(input())
for i in range(t):
    s = input()
    map = [0] * 1000
    for i in s:
        map[ord(i)] += 1
    res1 = ""
    res2 = ""
    for i in s:
        if map[ord(i)] == 1:
            res1 += i
        elif map[ord(i)] != 0:
            res2 += i
        map[ord(i)] = 0
    if len(res1) == 0:
        res1 = "NONE"
    if len(res2) == 0:
        res1 = "NONE"
    print(res1)
    print(res2)
