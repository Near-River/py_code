#############################################################################
class Fib(object):
    def __init__(self, num):
        self.num = num
        a, b, L = 0, 1, []
        L.append(a)
        for i in range(1, num):
            c = a + b
            a = b
            b = c
            L.append(a)
        Fib.nums = L

    def __str__(self):
        return str(Fib.nums)

    def __len__(self):
        return len(Fib.nums)


f = Fib(10)
print(f)
print(len(f))


#############################################################################
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        min_ = min(self.p, self.q)
        max_ = max(self.p, self.q)
        g = gcd(min_, max_)
        return '%d / %d' % (self.p / g, self.q / g)

    __repr__ = __str__


def gcd(a, b):  # 默认：a < b
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1.__div__(r2))
