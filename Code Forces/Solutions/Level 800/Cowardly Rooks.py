def cowardly_rooks():
    t = int(input())
    for i in range(t):
        board_size, no_rooks = map(int, input().split())
        for j in range(no_rooks):
            x1_rook, y1_rook = map(int, input().split())
        if board_size == no_rooks:
            print('NO')
        else:
            print('YES')


def main():
    cowardly_rooks()


main()
