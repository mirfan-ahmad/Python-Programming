def lexicographical():
    t1 = int(input())
    for i in range(t1):
        q = int(input())
        sa = la = lb = 'a'
        lena = lenb = 1
        for j in range(q):
            d, k, x = input().split()
            k = int(k)
            if d == '1':
                if max(x) > la:
                    la = max(x)
                lena += (k*len(x))
            else:
                if max(x) > lb:
                    lb = max(x)
                lenb += (k*len(x))
            if sa < lb:
                print('YES')
            elif la == lb:
                if lena < lenb:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')


lexicographical()
