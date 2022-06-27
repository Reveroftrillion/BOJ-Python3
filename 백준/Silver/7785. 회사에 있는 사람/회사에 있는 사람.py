import sys
input = sys.stdin.readline
# 주어진 n을 먼저 받는다.
A = int(input())
dict = {}
for i in range(A):
    a,b = map(str, input().split())
    if b == "enter":
        dict[a] = "In company"
    elif b == "leave":
        del dict[a]
# 딕셔너리를 사전 역순으로 작성하기
Dict = sorted(dict.keys(), reverse = True)
for j in Dict:
    print(j)