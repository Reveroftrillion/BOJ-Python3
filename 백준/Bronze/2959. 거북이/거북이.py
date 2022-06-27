A,B,C,D = map(int, input().split())
E = int(min(A,B,C,D))
list = [A,B,C,D]
list.remove(E)
F = int(max(list))
G = int(min(list))
list.remove(F)
list.remove(G)
H = list[0]
print(E*H)