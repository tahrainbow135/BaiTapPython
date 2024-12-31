class DoiThi:
    def __init__(self, ten, diem, sohieu, banthang):
        self.ten = ten
        self.diem = diem
        self.sohieu = sohieu
        self.banthang = banthang
    def __str__(self):
        return f'{self.ten} {self.diem} {self.sohieu} {self.banthang}'


t = int(input())
dsdt = []
for i in range(t):
    ten = input()
    a = list(map(int, input().split()))
    dsdt.append(DoiThi(ten, a[0], a[1], a[2]))
dsdt.sort(key = lambda dt : (-dt.diem, -dt.sohieu, -dt.banthang))
for i in dsdt:
    print(i)
