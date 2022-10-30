def Even_odd_increment():
    t = int(input())
    for i in range(t):
        len_arr, no_queries = map(int, input().split())
        elements = list(map(int, input().split()))
        for j in range(no_queries):
            tj, xj = map(int, input().split())
            if tj == 0:
                for k in range(len_arr):
                    if elements[k] % 2 == 0:
                        elements[k] += xj
            else:
                for m in range(len_arr):
                    if elements[m] % 2 == 1:
                        elements[m] += xj
            print(sum(elements))


def main():
    Even_odd_increment()


main()
