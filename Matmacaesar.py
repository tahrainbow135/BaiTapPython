t = int(input())
for i in range(t):
    s,k = input().split()
    k = int(k)
    res = ""
    for char in s:
        if char.islower():
            i =  chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            i =  chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        res += i
    print(res)


