A = int(input())
Request = 0
for i in range(1, A+1):
    if i < 100:
        Request += 1
    else:
        a = i//100
        b = i//10 - (a*10) 
        c = i - (a*100+b*10)
        if a-b == b-c:
            Request += 1
print(Request)