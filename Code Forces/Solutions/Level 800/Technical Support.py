def is_answered():
    t_cases = int(input())
    for i in range(t_cases):
        n = int(input())
        s = input()
        count = 0
        for j in range(n):
            if s[j] == 'Q':
                count += 1
            elif count >= 1:
                count -= 1
        if count == 0:
            print('Yes')
        else:
            print('No')


def main():
    is_answered()


main()
