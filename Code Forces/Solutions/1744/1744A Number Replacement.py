def number_replacement():
    t = int(input())
    for i in range(t):
        len_arr = int(input())
        elements = list(map(int, input().split()))
        string = input()
        for j in range(len_arr):
            a = elements[j]
            for k in range(len_arr):
                if elements[k] == a:
                    elements[k] = string[j]
        flag = 'Yes'
        for k in range(len_arr):
            if elements[k] != string[k]:
                flag = 'No'
                break
        print(flag)


def main():
    number_replacement()


main()
