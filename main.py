# 105064506 鄭柏偉
# XTR
from Point import Point


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


if __name__ == '__main__':
    p = int(delete_space('0ED63D1E 55533501 0A551576 3B2A9D57 DAD4CFE6 2E98A34B'), 16)
    q = int(delete_space('0B507397 0D0FEDC5 4F45BA84 36122A02 29C0CF9F B4F6D7'), 16)

    x1 = int(delete_space('05979DD0 F29B6D57 87458232 E258C35C 12898230 E4610C58'), 16)
    x2 = int(delete_space('0C328613 C13A98B2 42CEF504 BBFAAE70 15C6C0F4 D3BCF162'), 16)

    y1 = int(delete_space('9166EB14 BA0E8757 A9FBCF6A D13710AE A4EC4CF3 288A'), 16)
    y2 = int(delete_space('09C4B2B4 734B0E8B 24119D8C 350AC19F 199FDEB2 BA5DA6'), 16)

    X = Point(x1, x2, p)
    Y = Point(y1, y2, p)

    Z = X.__multi__(Y)
    Z.__show__()


