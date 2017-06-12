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
    p = int(delete_space('0ED63D1E 55533501 0A551576 3B2A9D57 DAD4CFE6 2E98A34B'), 16)
    q = int(delete_space('0B507397 0D0FEDC5 4F45BA84 36122A02 29C0CF9F B4F6D7'), 16)

    x = int(delete_space('05979DD0 F29B6D57 87458232 E258C35C 12898230 E4610C58'), 16)
    y = int(delete_space('0C328613 C13A98B2 42CEF504 BBFAAE70 15C6C0F4 D3BCF162'), 16)

    a = int(delete_space('9166EB14 BA0E8757 A9FBCF6A D13710AE A4EC4CF3 288A'), 16)
    b = int(delete_space('09C4B2B4 734B0E8B 24119D8C 350AC19F 199FDEB2 BA5DA6'), 16)

    C = {-1: Point(x, y, p).powerP(),
         0: Point(p - 3, p - 3, p),
         1: Point(x, y, p)}

    Cn(a).show()
    Cn(b).show()
    Cn((a * b) % q).show()

