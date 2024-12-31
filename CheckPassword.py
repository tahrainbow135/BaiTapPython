def check(s):
    if len(s) < 6 or len(s) > 12:
        return False
    check1, check2, check3, check4 = False, False, False, False
    for i in s:
        if i >= 'a' and i <= 'z':
            check1 = True
        elif i >= 'A' and i <= 'Z':
            check2 = True
        elif i >= '0' and i <= '9':
            check3 = True
        elif i in "$#@!":
            check4 = True
    if check1 and check2 and check3 and check4:
        return True
    return False

s = input()
l = s.split(",")
res = []
for tmp in l:
    if check(tmp):
        res.append(tmp)
if len(res) == 0:
    print("INVALID PASSWORD")
else:
    for i in range(0, len(res) - 1):
        print(res[i], sep= ",")
    print(res[len(res) - 1])
