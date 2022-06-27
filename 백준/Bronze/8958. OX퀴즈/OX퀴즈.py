A = int(input())
for i in range(A):
    B = input()
    C = list(B)
    sum = 0
    D = 1
    for i in C:
        if i == "O":
            sum+=D
            D+=1
        else:
            D=1
    print(sum)