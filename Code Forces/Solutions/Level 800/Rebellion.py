def Rebellion():
    t = int(input())
    for i in range(t):
        n = int(input())
        elements = list(map(int, input().split()))
        p1 = 0
        j = n-1
        count = 0
        while p1 < j:
            if elements[j] == 0 and elements[p1] == 1:
                elements[j] = 1
                elements.pop(p1)
                j -= 1
                count += 1
            elif elements[p1] == 1 or elements[j] == 1:
                j -= 1
            elif elements[j] == 0:
                p1 += 1
        print(count)


def main():
    Rebellion()


main()
