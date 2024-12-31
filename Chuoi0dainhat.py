t = int(input())
for i in range(t):
    s = input()
    tmp = 0
    res = 0
    for i in s:
        if i == '0':
            tmp += 1
        else:
            res = max(res, tmp)
            tmp = 0
    print(res)
