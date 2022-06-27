A = int(input())
count = dict()
# 딕셔너리에 책 이름은 key로 두고, 팔린 책의 개수를 value로 지정하자.
for i in range(A):
    B = input()
    if B in count:
        count[B] += 1
    else:
        count[B]=1
# value값 내림차순으로 정리해주기
Dict = dict(sorted(count.items()))
check = 0
for j in Dict:
    if (Dict[j]) > check:
        check = Dict[j]
        want = j
print(want)