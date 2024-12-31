t = int(input())
for i in range(t):
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    if len(v1) != len(v2):
        print("INVALID")
    else:
        xh = [0] * 1000
        dem = 0
        for i in v1:
            xh[i] += 1
        for i in v2:
            if xh[i] > 0:
                dem += 1
                xh[i] = 0
        dem2 = set(v1 + v2)
        res = dem / len(dem2)
        print('%.5f' %res)