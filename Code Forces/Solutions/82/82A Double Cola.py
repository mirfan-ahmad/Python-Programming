def double_cola():
    n = int(input())
    i = 0
    v = pow(2, i) * 5
    persons = {1: 'Sheldon', 2: 'Leonard', 3: 'Penny', 4: 'Rajesh', 5: 'Howard'}
    if n > 5:
        while True:
            if v > n:
                value = int(n - (v - (pow(2, i) * 5)))
                count = 1
                while True:
                    if value <= pow(2, i):
                        return persons[count]
                    elif value - pow(2, i) < pow(2, i):
                        count += 1
                        break
                    count += 1
                    value -= pow(2, i)
                break
            elif v == n:
                return persons[5]
            i += 1
            v += pow(2, i) * 5
    else:
        count = n % 5 if n < 5 else n
    return persons[count]


print(double_cola())
