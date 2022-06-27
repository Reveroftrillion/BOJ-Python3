t = int(input())
res = 0
for i in range(t):
    res = 0
    sol = list(input().split())
    for j in sol:
        if j == sol[0]:
            res += float(j)
        else:
            if j == '@':
                res *= 3
            elif j == '%':
                res += 5
            elif j == '#':
                res -= 7
    print('%.2f' %res)