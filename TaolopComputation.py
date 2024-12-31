import math


class Computation:
    def __init__(self, n):
        self.n = n

    def Factorial(self):
        if self.n == 0:
            return 1
        res = 1
        for i in range(1, self.n):
            res *= i
        return res

    def Prime(self):
        if self.n < 2:
            return "NO"
        if self.n != 2 and self.n % 2 == 0:
            return "NO"
        if self.n != 3 and self.n % 3 == 0:
            return "NO"
        else:
            tmp = int(math.sqrt(self.n) + 1)
            for i in range(5,tmp, 6):
                if self.n % i == 0 or self.n % (i + 2) == 0:
                    return "NO"
        return "YES"

    def listDiv(self):
        res = set()
        tmp = int(math.sqrt(self.n) + 1)
        for i in range(1, tmp):
            if self.n % i == 0:
                res.add(i)
                res.add(self.n // i)
        print(','.join(map(str,res)))

    def __str__(self):
        return f'{self.Factorial()}\n{self.Prime()}'

n = int(input())
tinhn = Computation(n)
print(tinhn)
tinhn.listDiv()