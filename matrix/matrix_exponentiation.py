#*****matrix exponentiation*****

x = int(input())

matrix1 = [[int(n) for n in input().split()] for j in range(x)]

exp = int(input())

res = [[1 if i == j else 0 for j in range(x)] for i in range(x)]

for g in range(exp):
    matrix3 = [[0] * x for _ in range(x)]
    for i in range(x):
        for r in range(x):
            for j in range(x):
                matrix3[i][r] += (int(res[i][j]) * int(matrix1[j][r]))
    res = matrix3
for row in res:
    print(*row)