import json
try:
    with open("tips.json","r") as f:
        data = json.load(f)["tips"]
except FileNotFoundError:
    print("Invalid")
except json.JSONDecodeError:
    print("Invalid")
agv = 0
t = int(input())
for _ in range(t):
    day, size = input().split()
    res = []
    for tip in data:
        if day == tip["day"] and size == tip["size"]:
            res.append(float(tip["total_bill"]))
    if len(res) == 0:
        print("Invalid")
    else:
        ans = sum(res) / len(res)
        print('%.4f' %ans)
