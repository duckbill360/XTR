# class Point


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


class Point:

    def __init__(self, x, y, p):
        # x is the coefficient of alpha
        # y is the coefficient of alpha^2
        # p defines the field
        self.p = p
        self.x = x % self.p
        self.y = y % self.p

    def __hash__(self):
        return hash((self.x, self.y))

    def add(self, other):
        return Point((self.x + other.x) % self.p,
                     (self.y + other.y) % self.p,
                     self.p)

    def sub(self, other):
        return Point((self.x - other.x) % self.p,
                     (self.y - other.y) % self.p,
                     self.p)

    def multi(self, other):
        return Point((-self.x * other.y - self.y * other.x + self.y * other.y) % self.p,
                     (self.x * other.x - self.x * other.y - self.y * other.x) % self.p,
                     self.p)

    def scalar_multi(self, scalar):
        return Point(self.x * scalar, self.y * scalar, self.p)

    def powerP(self):
        return Point(self.y, self.x, self.p)

    def show(self):
        print('x:', add_space(format(self.x, 'x')))
        print('y:', add_space(format(self.y, 'x')))


