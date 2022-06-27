list = []
for i in range (0,9):
    list.append(int(input()))
A = max(list)
print(A)
print(list.index(A)+1)