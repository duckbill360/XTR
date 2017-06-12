# 105064506 鄭柏偉
# XTR
from Point import Point
from functools import lru_cache


def delete_space(string):
    lst = string.split(' ')
    output = ''
    for i in lst:
        output += i
    return output


def add_space(string):
    string = string[::-1]
    string = ' '.join(string[i:i + 8] for i in range(0, len(string), 8))
    return string[::-1]


@lru_cache(maxsize=None)
def Cn(n):
    if n == -1 or n == 0 or n == 1:
        return C[n]
    elif n % 2 == 0:
        m = n // 2
        return Cn(m).multi(Cn(m)).sub(Cn(m).powerP().scalar_multi(2))
    elif n % 2 == 1:
        m = (n - 1) // 2
        return Cn(m + 1).multi(Cn(m)).sub(C[1].multi(Cn(m).powerP())).add(Cn(m - 1).powerP())


if __name__ == '__main__':
    p = int(delete_space(input('p =')), 16)
    q = int(delete_space(input('q =')), 16)

    x = int(delete_space(input('Tr(g).x =')), 16)
    y = int(delete_space(input('Tr(g).y =')), 16)

    a = int(delete_space(input('a =')), 16)
    b = int(delete_space(input('b =')), 16)

    C = {-1: Point(x, y, p).powerP(),
         0: Point(p - 3, p - 3, p),
         1: Point(x, y, p)}

    Cn(a).show()
    Cn(b).show()
    Cn((a * b) % q).show()

