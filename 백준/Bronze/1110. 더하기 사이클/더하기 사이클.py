N = m = int(input())
cnt = 0
while True:
    a = N//10
    b = N%10
    c = a+b
    cnt+=1
    N = b*10+c%10
    if N == m:
        break
print(cnt)