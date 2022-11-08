from math import ceil


def Theatre_Square():
    m, n, a = map(int, input().split())
    r = m / a
    c = n / a
    print(ceil(r) * ceil(c))


Theatre_Square()
