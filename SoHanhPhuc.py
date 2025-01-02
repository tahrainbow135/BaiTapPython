n = input()
ok = 0
visit = set()
while n != "1":
    if len(n) == 1 and n != "1":
        ok = 1
        break
    if n in visit:
        ok = 1
        break
    res = 0
    for i in n:
        res += int(i) ** 2
    visit.add(n)
    n = str(res)

if ok == 1:
    print("NO")
else:
    print("YES")