def maxmina():
    t = int(input())
    for i in range(t):
        size_arr, len_segment = map(int, input().split())
        elements = list(map(int, input().split()))
        for j in range(size_arr):
            if elements[j] == 1:
                print('Yes')
                break
        else:
            print('NO')


maxmina()
