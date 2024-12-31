import pandas as pd

try:
    df = pd.read_csv("penguins.csv")
except FileNotFoundError:
    print("Invalid")
    exit()

t = int(input())
for _ in range(t):
    ten, quocgia = input().split()

    # Lọc dữ liệu dựa trên loài và hòn đảo
    filtered_df = df[(df["species"] == ten) & (df["island"] == quocgia)]

    # Lọc cột chiều dài và chiều sâu mỏ
    res1 = filtered_df["bill_length_mm"].dropna().astype(float)
    res2 = filtered_df["bill_depth_mm"].dropna().astype(float)

    if res1.empty or res2.empty:
        print("Invalid")
    else:
        print(f'{res1.sum()/len(res1):.4f} {res2.mean():.4f}')
