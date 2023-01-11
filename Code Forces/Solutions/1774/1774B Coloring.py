def coloring():
    n, m, k = map(int, input().split())
    color_used = list(map(int, input().split()))
    if n % k == 0:
        max_freq = n/k
        max_element = k
    else:
        max_freq = (n/k) + 1
        max_element = n % k

    for color in color_used:
        if color > max_freq:
            max_element = -1
        elif color == max_freq:
            max_element -= 1
    if max_element < 0:
        return 'No'
    return 'Yes'


t = int(input())
for i in range(t):
    print(coloring())
