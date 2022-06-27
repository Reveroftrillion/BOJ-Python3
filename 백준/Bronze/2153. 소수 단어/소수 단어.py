import math
word = list(input())
num = 0
for i in word:
    if ord(i)<94:
        num+=(ord(i)-38)
    else:
        num+=(ord(i)-96)
for i in range (2, int(math.sqrt(num)+1)):
    if num%i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")