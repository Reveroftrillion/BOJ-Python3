def push(a):
    list.append(a)
def pop():
    if len(list) == 0:
        return(-1)
    else:
        return list.pop()
def size():
    return(len(list))
def empty():
    if len(list) == 0:
        return(1)
    else:
        return(0)
def top():
    if len(list) == 0:
        return(-1) 
    else:
        return(list[-1])
import sys
input = sys.stdin.readline
A = int(input())
list = []
for _ in range(A):
    come = input().rstrip().split()
    want = come[0]
    if want == "push":
        push(come[1])
    elif want == "pop":
        print(pop())
    elif want == "size":
        print(size())
    elif want == "empty":
        print(empty())
    elif want == "top":
        print(top())