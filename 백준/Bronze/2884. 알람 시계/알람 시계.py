A,B = map(int, input().split())
if(A>=0 and B>=45):
    print(A, B-45)
elif(A>0 and B>=0):
    print(A-1, B+15)
else:
    print(23, B+15)