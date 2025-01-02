from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
k = int(input())
dict = defaultdict(list)
for i in range(n):
    dict[a[i]].append(i)
if len(dict[k]) == 0:
    print(-1)
else:
    print(','.join(map(str,dict[k])))