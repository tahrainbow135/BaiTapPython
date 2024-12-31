from datetime import datetime


class NhanVien:
    def __init__(self, mnv, ten, giovao, giora):
        self.mnv = mnv
        self.ten = ten
        giovao = datetime.strptime(giovao, "%H:%M")
        giora = datetime.strptime(giora, "%H:%M")
        self.gio = giora - giovao
        self.hh = int(self.gio.total_seconds() // 3600) - 1
        self.mm = int((self.gio.total_seconds() % 3600) // 60)
        self.res = self.tinhres()

    def tinhres(self):
        if self.gio.total_seconds() >= 8 * 3600:
            return "Du"
        else:
            return "Thieu"

if __name__ == "__main__":
    t = int(input())
    dsnv = []
    for i in range(t):
        mnv = input()
        ten = input()
        giovao = input()
        giora = input()
        dsnv.append(NhanVien(mnv, ten, giovao, giora))

    # Sắp xếp theo thời gian làm việc giảm dần
    dsnv.sort(key=lambda nv: nv.gio.total_seconds(), reverse=True)

    for nv in dsnv:
        print(nv.mnv, nv.ten, nv.hh, "gio", nv.mm, "phut", nv.res, sep=" ")
