A = int(input())
for i in range(A):
    B = input()
    C = list(B)
    num = 0
    # C의 요소 중 (가 등장하면 +2, )가 등장하면 -2하자
    for j in C:
        if j =="(":
            num += 2
        else:
            num -= 2
        # sum이 0보다 작아진다면 NO를 프린트하자
        if num<0:
            print("NO")
            break
    # num이 0이 아니라면 NO를 프린트하자
    if num>0:
        print("NO")
    elif num == 0:
        print("YES")        