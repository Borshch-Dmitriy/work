#*****matrices addition*****

x,y = map(int,input().split())

matrix1 = [input().split() for j in range(x)]
input()
matrix2 = [input().split() for i in range(x)]

for i in range(x):
    result = [int(matrix1[i][j]) + int(matrix2[i][j]) for j in range(y)]
    print(*result)