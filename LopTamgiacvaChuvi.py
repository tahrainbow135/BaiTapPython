import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def khoangcach(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


class Tamgiac:
    def __init__(self, a, b, c):
        self.points = [a, b, c]

    def tinhchuvi(self):
        kc1 = self.points[0].khoangcach(self.points[1])
        kc2 = self.points[0].khoangcach(self.points[2])
        kc3 = self.points[1].khoangcach(self.points[2])
        if kc1 + kc2 <= kc3 or kc1 + kc3 <= kc2 or kc2 + kc3 <= kc1:
            return "INVALID"
        else:
            return '{:.6f}'.format(kc1 + kc2 + kc3)


t = int(input())

for i in range(t):
    l = list(map(float, input().split()))
    a = Point(l[0], l[1])
    b = Point(l[2], l[3])
    c = Point(l[4], l[5])
    tg = Tamgiac(a, b, c)
    print(tg.tinhchuvi(), end=" ")