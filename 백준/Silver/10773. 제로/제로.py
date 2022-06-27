A = int(input())
list = []
for i in range(A):
    B = int(input())
    if B == 0:
        list.pop()
    else:
        list.append(B)
print(sum(list))