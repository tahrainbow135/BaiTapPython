t = int(input())
for i in range(t):
    s = input()
    tich = 1
    sum = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            tich *= int(s[i])
        else:
            sum += int(s[i])
    res = "INVALID" if sum == 0 else tich / sum
    print('%.6f' %res)
    