n = int(input())
arr = list(map(int, input().split()))

MAX_VAL = max(arr)
freq = [0] * (MAX_VAL + 1)
for num in arr:
    freq[num] += 1
st = [num for num in range(MAX_VAL + 1) if freq[num] > 0]

count = 0
for i in range(len(st)):
    x = st[i]
    count += freq[x] * (freq[x] - 1) // 2

    for j in range(i + 1, len(st)):
        y = st[j]
        product = x * y
        is_lucky = False
        for k in range(2, 4):
            if (pow(x, k) + pow(y, k)) % product == 0:
                is_lucky = True
                break

        if is_lucky:
            count += freq[x] * freq[y]

print(count)
