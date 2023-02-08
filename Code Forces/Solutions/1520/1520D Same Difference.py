# def SameDifference():
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         count = 0
#         k = 0
#         for j in range(n-1):
#         for j in range(k+1, n):
#             if arr[j] - arr[k] == j - k:
#                 count += 1
#
#         print(count)
#
#
# SameDifference()

import itertools


def SameDifference():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        comb = list(itertools.combinations(arr, 2))
        br = 1
        count = 0
        k = 1
        for j in range(len(comb)):
            if comb[j][1] - comb[j][0] == br:
                count += 1
            br += 1
            if br > n - k:
                br = 1
                k += 1

        print(count)


SameDifference()
