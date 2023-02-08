def Two_Groups():
    t = int(input())
    for i in range(t):
        len_arr = int(input())
        arr = list(map(int, input().split()))
        a, b = [], []
        for j in range(len_arr):
            if arr[j] >= 0:
                a.append(arr[j])
            else:
                b.append(arr[j])
        print(abs(sum(a)-abs(sum(b))))


Two_Groups()
