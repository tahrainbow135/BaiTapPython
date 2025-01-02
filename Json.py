import json

try:
    with open("flights.json", "r", encoding="utf-8") as f:
        data = json.load(f)["flights"]
except FileNotFoundError:
    print("Invalid")
    exit()
except json.JSONDecodeError:
    print("Invalid")
    exit()

t = int(input())

for _ in range(t):
    year, yc = input().split()

    # Lọc dữ liệu theo năm
    res = [int(flight["passengers"]) for flight in data if flight["year"] == year]

    if not res:
        print("Invalid")
        continue

    if yc == "min":
        print(min(res))
    elif yc == "max":
        print(max(res))
    elif yc == "sum":
        print(sum(res))
    elif yc == "avg":
        print(f"{sum(res) / len(res):.5f}")
    else:
        print("Invalid")