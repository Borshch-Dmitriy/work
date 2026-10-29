#*****matrix multiplication*****

x,y = map(int,input().split())
matrix1 = [input().split() for j in range(x)]

input()
x1,y1 = map(int,input().split())
matrix2 = [input().split() for i in range(x1)]

matrix3 = [[0] * y1 for _ in range(x)]

for i in range(x):
    for r in range(y1):
        for j in range(y):
            matrix3[i][r] += (int(matrix1[i][j]) * int(matrix2[j][r]))

for r in matrix3:
    print(*(k for k in r))