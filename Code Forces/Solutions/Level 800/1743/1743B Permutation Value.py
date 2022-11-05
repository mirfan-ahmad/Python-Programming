def print_permutations(m, n):
    while m < n:
        if m == n - 1:
            print(m, n)
        else:
            print(m, n, end=" ")
        m += 1
        n -= 1
    return m


def permutation_value():
    t = int(input())
    for i in range(t):
        n = int(input())
        m = 1
        if n % 2 == 0:
            print_permutations(m, n)
        else:
            m = print_permutations(m, n)
            print(m)


permutation_value()
