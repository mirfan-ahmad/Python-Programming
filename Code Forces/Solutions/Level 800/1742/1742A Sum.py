def Sum():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        if a + b == c:
            print('Yes')
        elif a + c == b:
            print('Yes')
        elif b + c == a:
            print('Yes')
        else:
            print('No')


def main():
    Sum()


main()
