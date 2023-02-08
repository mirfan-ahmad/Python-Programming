from itertools import combinations


def Books():
    n, t = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    seq = []
    book_read = []
    if arr[0] > t:
        return 0
    elif sum(arr) < t:
        return len(arr)
    for i in range(len(arr) + 1):
        seq += combinations(arr, i)
    for j in range(len(seq)):
        if sum(seq[j]) == t:
            book_read.append(len(seq[j]))
    return max(book_read)


print(Books())
