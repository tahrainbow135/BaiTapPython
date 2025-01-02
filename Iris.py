import csv

try:
    with open("iris.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # Đọc dòng tiêu đề
        if not header:
            raise ValueError("File is empty or invalid")
        data = [row for row in reader]
        # print(*data)
except FileNotFoundError:
    print("Invalid")
    exit()
except Exception:
    print("Invalid")
    exit()

header_to_index = {header[i]: i for i in range(len(header))}

valid_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

t = int(input())
for _ in range(t):
    teny, chieux, yc = input().split()
    res = []

    if chieux in valid_columns:
        for row in data:
            if row[header_to_index["species"]] == teny:
                try:
                    res.append(float(row[header_to_index[chieux]]))
                except ValueError:
                    print("Invalid")
                    break
    else:
        print("Invalid")
        continue

    if len(res) == 0:
        print("Invalid")
    else:
        if yc == "min":
            print(min(res))
        elif yc == "max":
            print(max(res))
        elif yc == "sum":
            print(sum(res))
        elif yc == "avg":
            print(f'{sum(res) / len(res):.2f}')
        else:
            print("Invalid")
