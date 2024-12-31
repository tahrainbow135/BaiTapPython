import math

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if len(a) != len(b):
        print("INVALID")
    else:
        res = math.sqrt(sum((b[j] - a[j]) ** 2 for j in range(len(a))))
        print('%.5f' %res)


