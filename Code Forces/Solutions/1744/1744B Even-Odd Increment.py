def even_odd_increment():
    t = int(input())
    for i in range(t):
        len_arr, no_of_queries = map(int, input().split())
        elements = list(map(int, input().split()))
        even, odd = 0, 0
        for e in elements:
            if e % 2 == 0:
                even += 1
            else:
                odd += 1
        increment = 0
        sum_array = sum(elements)
        for j in range(no_of_queries):
            tj, xj = map(int, input().split())
            if tj == 0:
                if xj % 2 == 0:
                    x = even * xj
                    increment += x
                else:
                    x = even * xj
                    increment += x
                    odd += even
                    even = 0
            else:
                if xj % 2 == 0:
                    x = odd * xj
                    increment += x
                else:
                    x = odd * xj
                    increment += x
                    even += odd
                    odd = 0
            print(sum_array + increment)


even_odd_increment()
