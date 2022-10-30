def number_replacement():
    t = int(input())
    for i in range(t):
        len_arr = int(input())
        a = list(map(int, input().split()))
        elements = set(a)
        string = input()
        for k in range(len_arr):
            a[k] = string[k]
        if len(elements) >= len(string):
            print('Yes')
        else:
            print('No')


def main():
    number_replacement()


main()
