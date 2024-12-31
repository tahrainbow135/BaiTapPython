t = int(input())
for i in range(t):
    sum = 0.0
    n = int(input())
    if n%2==0:
        for x in range(2, n + 1, 4):
            sum += 1/x
        for x in range(4, n + 1, 4):
            sum -= 1/x
    else:
        for x in range(1, n + 1, 4):
            sum += 1 / x
        for x in range(3, n + 1, 4):
            sum -= 1 / x
    print('%.5f'%sum)