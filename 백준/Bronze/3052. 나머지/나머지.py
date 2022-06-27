list = []
for i in range(10):
    A = int(input())
    list.append(A%42)
list = set(list)
print(len(list))