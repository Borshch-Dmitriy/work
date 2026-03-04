#Filling the matrix in snake case!!!!!!
x,y = map(int,input().split())

matrix = [[0] * y for i in range(x)]

counter = 1
for i in range(x):
    step = y - 1
    for j in range(y):
        if i % 2 == 0:
            matrix[i][j] = counter
            counter += 1
        elif i % 2 == 1:
            matrix[i][j+step] = counter
            counter += 1
            step -= 2

for j in matrix:
        print(*(str(k).ljust(2) for k in j))
