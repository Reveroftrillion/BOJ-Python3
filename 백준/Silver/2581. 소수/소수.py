import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = dict()
for i in range(A,B+1):
    if i > 1:
        for j in range(2,i):
            # 여기서 anything은 소수아닌 것을 처리할 방법이 없어서 넣어둔거임    
            anything = 0
            if i%j == 0:
                anything += 1
                break
        else:
            C[i] = 1   
# dict의 길이가 0이라면 -1 출력
# dict의 길이가 0이 아니라면 리스트에 key 추가하고 key의 sum과 min을 출력하기
if len(C) != 0:
    list = []
    for keys in C:
        list.append(keys)
    print(sum(list))
    print(min(list))
else:
    print(-1)