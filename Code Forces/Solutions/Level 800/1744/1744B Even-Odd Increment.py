def Even_odd_increment():
    t = int(input())
    for i in range(t):
        len_arr, no_queries = map(int, input().split())
        elements = list(map(int, input().split()))
        even_array = list(filter(lambda x: x % 2 == 0, elements))
        odd_array = list(filter(lambda x: x % 2 == 1, elements))
        for j in range(no_queries):
            tj, xj = map(int, input().split())
            if tj == 0:
                # for k in range(len_arr):
                #     if elements[k] % 2 == 0:
                #         elements[k] += xj
                if xj % 2 == 0:
                    for k in range(len(even_array)):
                        even_array[k] += xj
                else:
                    k = 0
                    while k < len(even_array):
                        odd_array.append(even_array[k] + xj)
                        even_array.pop(k)
            else:
                # for m in range(len_arr):
                #     if elements[m] % 2 == 1:
                #         elements[m] += xj
                if xj % 2 == 0:
                    for k in range(len(odd_array)):
                        odd_array[k] += xj
                else:
                    k = 0
                    while k < len(odd_array):
                        even_array.append(odd_array[k] + xj)
                        odd_array.pop(k)
            print(sum(even_array) + sum(odd_array))


def main():
    Even_odd_increment()


main()
