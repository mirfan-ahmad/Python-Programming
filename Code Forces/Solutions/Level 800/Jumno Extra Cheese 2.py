def Jumbo_Extra_Cheese():
    t = int(input())
    for i in range(t):
        slices = int(input())
        array_x = []
        array_y = []
        for j in range(slices):
            n, m = map(int, input().split())
            if n < m:
                n, m = m, n
            array_x.append(m)
            array_y.append(n)
        print((max(array_y)*2)+(sum(array_x)*2))


def main():
    Jumbo_Extra_Cheese()


main()
