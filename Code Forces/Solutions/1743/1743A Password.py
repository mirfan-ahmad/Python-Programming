def password():
    t = int(input())
    for i in range(t):
        len_digits = int(input())
        not_used = list(map(int, input().split()))
        used = 10 - len_digits
        print(int(6 * (used * (used-1)/2)))


def main():
    password()


main()
