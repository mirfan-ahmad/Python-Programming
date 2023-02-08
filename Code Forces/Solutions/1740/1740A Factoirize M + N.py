def next_prime(n):
    p = n + 1
    for i in range(2, p):
        if p % i == 0:
            p = p + 1
    else:
        return p


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def check():
    t = int(input())
    for i in range(t):
        n = int(input())
        m = 1
        while True:
            m = next_prime(m)
            if m != n and not is_prime(n + m):
                print(m)
                break


def main():
    check()


main()
