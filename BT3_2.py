t = int(input())
for i in range(t):
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    if len(v1) != len(v2):
        print("INVALID")
    else:
        res = sum(abs(v1[j] - v2[j]) for j in range(len(v1)))
        print('%.5f' %res)
    