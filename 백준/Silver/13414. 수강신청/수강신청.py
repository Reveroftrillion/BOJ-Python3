import sys
input = sys.stdin.readline
A,B = map(int, input().split())
C = dict()
num = 1
for i in range(B):
    Person = input().rstrip()
    C[Person] = num
    num+=1
C = sorted(C.items(), key = lambda item: item[1])
consider = 0
for answer, count in C:
    if consider == A:
        break
    print(answer)
    consider += 1