# class Point


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


class Point:

    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, other):
        return Point((self.x + other.x) % self.p,
                     (self.y + other.y) % self.p,
                     self.p)

    def __sub__(self, other):
        return Point((self.x - other.x) % self.p,
                     (self.y - other.y) % self.p,
                     self.p)

    def __multi__(self, other):
        return Point((-self.x * other.y - self.y * other.x + self.y * other.y) % self.p,
                     (self.x * other.x - self.x * other.y - self.y * other.x) % self.p,
                     self.p)

    def __show__(self):
        print('x:', add_space(format(self.x, 'x')))
        print('y:', add_space(format(self.y, 'x')))


