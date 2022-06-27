A = int(input())
math_cards = map(int, input().split())
B = int(input())
want = map(int, input().split())
standard = dict()
for math_card in math_cards:
    if math_card in standard:
        standard[math_card] += 1
    else:
        standard[math_card] = 1
for what_i_want in want:
    answer = standard.get(what_i_want)
    if answer != None:
        print(answer, end = " ")
    else:
        print("0", end = " ")