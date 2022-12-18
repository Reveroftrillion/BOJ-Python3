X = int(input())
N = int(input())
sum = 0
for i in range(1,N+1):
    a,b = input().split()
    sum += int(a)*int(b)
if X == sum:
    print("Yes")
else:
    print("No")