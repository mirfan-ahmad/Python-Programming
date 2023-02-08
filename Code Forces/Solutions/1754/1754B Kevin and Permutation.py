def kevin_permutation():
    t = int(input())
    for i in range(t):
        size = int(input())
        size1 = size
        if size % 2 == 1:
            for j in range(size1//2):
                print(f"{(size + 2)//2} {j+1} ", end="")
                size += 2
            print(size1)
        else:
            s = size // 2 + 1
            for j in range(size1//2):
                if j < (size//2)-1:
                    print(f"{s+j} {j+1} ", end="")
                else:
                    print(f"{s+j} {j+1}")


kevin_permutation()
