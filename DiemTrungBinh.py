class ThiSinh:
    def __init__(self, ten, ns, diem1, diem2, diem3):
        self.ten = ten
        self.ns = ns
        thap = min(diem1, diem2, diem3)
        self.tb = (diem1 + diem2 + diem3 + thap) / 4
if __name__ == "__main__":
    t = int(input())
    dsts = []
    for i in range(t):
        dsts.append(ThiSinh(input(), input(), float(input()), float(input()), float(input())))
    dsts.sort(key= lambda ts: ts.tb, reverse = True)
    for i in dsts:
        print(i.ten, i.ns, '%.1f' %i.tb)