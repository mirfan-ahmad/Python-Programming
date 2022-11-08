def xenia():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    unit = arr[0]-1
    for i in range(1, m):
        if arr[i] > arr[i-1]:
            unit += (arr[i] - arr[i-1])
        elif arr[i] < arr[i-1]:
            unit += (n-arr[i-1]) + (arr[i])
    print(unit)


xenia()
