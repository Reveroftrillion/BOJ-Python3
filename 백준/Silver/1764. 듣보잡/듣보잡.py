a,b = map(int, input().split())
list1 = []
for i in range(1,a+1):
    list1.append(input())
list2 = []
for j in range(1,b+1):
    list2.append(input())
set1 = set(list1)
set2 = set(list2)
LIST = sorted(list(set1 & set2))
print(len(LIST))
for l in LIST:
    print(l)