t = int(input())
for i in range(t):
    s = input()
    map = [0] * 1000
    for i in s:
        map[ord(i)] += 1
    res = max(map)
    for i in s:
        if map[ord(i)] == res:
            print(i)
            break
