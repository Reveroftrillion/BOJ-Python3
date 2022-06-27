A = int(input())
B = 0
while A>=0:
    if A%5 == 0:
        B += (A//5)
        print(B)
        break
    A -= 3
    B += 1
else:
    print(-1)