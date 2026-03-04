#Filling the matrix by diagonals!!!!!!
#******example*****
#1   2   4   7   10
#3   5   8   11  13
#6   9   12  14  15
#******************
x,y = map(int,input().split())
matrix = [[0] * y for i in range(x)]
counter = 1

for s in range(x + y - 1):
    for i in range(x):
        j = s - i
        if 0 <= j < y:
            matrix[i][j] = counter
            counter += 1

for j in matrix:
        print(*(str(k).ljust(3) for k in j))

