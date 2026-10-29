# Spiral Matrix
#****example***
#* 1  2  3  4 *
#* 12 13 14 5 *
#* 11 16 15 6 *
#* 10 9  8  7 *
#**************
x,y = map(int,input().split())

matrix = [[0] * y for i in range(x)]
counter = 1

top_border = 0
bottom_border = x-1
left_border = 0
right_border = y-1

while (x * y) >= counter:
    for j in range(left_border, right_border + 1):
        matrix[top_border][j] = counter
        counter += 1
    top_border += 1
    if (x * y) >= counter:
        for i in range(top_border, bottom_border + 1):
            matrix[i][right_border] = counter
            counter += 1
        right_border -= 1
    if (x * y) >= counter:
        for j in range(right_border, left_border - 1, -1):
            matrix[bottom_border][j] = counter
            counter += 1
        bottom_border -= 1
    if (x * y) >= counter:
        for i in range(bottom_border, top_border - 1, -1):
            matrix[i][left_border] = counter
            counter += 1
        left_border += 1
for i in matrix:
    print(*(str(j).ljust(2) for j in i))