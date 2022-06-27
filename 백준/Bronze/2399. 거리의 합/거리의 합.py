# sys.stdin.readline을 사용하기 위한 준비
import sys
# 점의 개수를 받는다
A = int(input())
# 리스트 생성하고 리스트에 주어진 숫자 넣어두기
N = map(int, sys.stdin.readline().split())
M = sorted(N)
O = len(M)
sum = 0
# 두 수 차이를 뒤에서 한 번, 앞에서 한 번씩 빼준다.
for i in range(1, O):
    sum+=(M[i]-M[i-1])*i*(O-i)*2
print(sum)