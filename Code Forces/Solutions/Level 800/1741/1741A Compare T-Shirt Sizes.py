def Compare_size():
    t = int(input())
    for i in range(t):
        a, b = input().split()
        dic = {"S": -1, "M": 0, "L": 1}
        ca, cb = len(a[:-1]), len(b[:-1])
        if a == b:
            print('=')
        elif a[-1] == b[-1]:
            ca *= dic[a[-1]]
            cb *= dic[b[-1]]
            if ca > cb:
                print('>')
            else:
                print('<')
        else:
            if a[-1] == 'S':
                print('<')
            elif b[-1] == "S":
                print('>')
            elif a[-1] == "L":
                print(">")
            elif b[-1] == 'L':
                print('<')


Compare_size()
