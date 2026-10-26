# find the trace of matrix(addition of all numbers in main diagonal)
row = int(input())
matrix = []
result = 0
for r in range(row):
    matrix.append(input().split(" "))
for i in range(row):
    for j in range(row):
        if i == j:
            result += int(matrix[i][j])
        else:
            continue
print(result)
