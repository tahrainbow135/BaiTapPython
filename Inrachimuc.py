import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
x = int(input())
res = np.where(a == x)[0]
if len(res) > 0:
    print(",".join(map(str,res)))
else:
    print("-1")

