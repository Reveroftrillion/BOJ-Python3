a,b = map(int, input().split())
list = list()
for i in range(1,b+1):
    c = a*i
    c = (str(c)[::-1])
    c = c.lstrip('0')
    list.append(int(c))
print(max(list))