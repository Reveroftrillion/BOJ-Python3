def d(n):
    a = str(n)
    list_a = list(a)
    num = 0
    for i in list_a:
        num += int(i)
    return num+n

set1 = set()
set2 = set(k for k in range(1,10000))
for j in range(1,10000):
    set1.add(d(j))
#for k in range(1,10000):
    #set2.add(k)
want = set(set2 - set1)
for answer in sorted(want):
    print(answer)