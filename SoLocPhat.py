t = int(input())
for i in range(t):
    s = input()
    tmp = s[len(s) - 3: len(s)]
    if tmp == "668":
        print("YES")
    else:
        print("NO")