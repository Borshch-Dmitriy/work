#Filling the matrix in snake case!!!!!!
x,y = map(int,input().split())
matrix = [[0] * y for i in range(x)]
counter = 1

for i in range(x):
    if i % 2 == 0:
        for j in range(y):
            matrix[i][j] = counter
            counter += 1
    else:
        for j in range(y - 1, -1, -1):
            matrix[i][j] = counter
            counter += 1

for j in matrix:
        print(*(str(k).ljust(2) for k in j))
