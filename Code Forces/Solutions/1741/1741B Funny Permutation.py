def funny_Permutation():
    t = int(input())
    for i in range(t):
        f = int(input())
        if f == 3:
            print(-1)
        elif f % 2 == 0:
            for j in range(f, 0, -1):
                if j == 1:
                    print(j)
                else:
                    print(j, end=" ")
        elif f % 2 == 1:
            for j in range(f, f//2+1, -1):
                print(j, end=" ")
            for k in range(1, f//2+2):
                if k == f//2+1:
                    print(k)
                else:
                    print(k, end=" ")


funny_Permutation()
