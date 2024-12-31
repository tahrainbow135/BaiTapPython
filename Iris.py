import pandas as pd
try:
    df = pd.read_csv("iris.csv")
except FileNotFoundError:
    print("Invalid")
    exit()

t = int(input())
for _ in range(t):
    teny, chieux, yc = input().split()
    tmp = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    res = []
    if chieux in tmp:
        for _,hoa in df.iterrows():
            if hoa["species"] == teny:
                try:
                    res.append(float(hoa[chieux]))
                except ValueError:
                    print("Invalid")
    else:
        print("Invalid")
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
            print('%.2f' %(sum(res) / len(res)))
        else:
            print("Invalid")

