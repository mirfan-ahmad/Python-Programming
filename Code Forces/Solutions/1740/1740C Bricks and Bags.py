def Bricks_Bags():
    t = int(input())
    for i in range(t):
        bricks = int(input())
        weights = list(map(int, input().split()))
        b = max(weights)
        weights.remove(b)
        a = max(weights)
        c = min(weights)
        print(abs(a - b) + abs(b - c))


def main():
    Bricks_Bags()


main()
