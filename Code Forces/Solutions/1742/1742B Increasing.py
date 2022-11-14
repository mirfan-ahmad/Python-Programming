def increasing():
    t = int(input())
    for i in range(t):
        size = int(input())
        elements = list(map(int, input().split()))
        emp = []
        flag = 'Yes'
        for j in range(size):
            if elements[j] in emp:
                flag = 'No'
                break
            else:
                emp.append(elements[j])
        print(flag)


increasing()
