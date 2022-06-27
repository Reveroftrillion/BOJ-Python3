A = int(input())
def hanoi(a,b,c,d):
    if a != 1:
        hanoi(a-1,b,d,c)
        hanoi(1,b,c,d)
        hanoi(a-1,c,b,d)
    else:
        print(b, d)
print(2**A-1)
if A <= 20:
    hanoi(A,1,2,3)