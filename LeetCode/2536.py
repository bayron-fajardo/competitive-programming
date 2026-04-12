n = 3
mat = [[0] * (n+1) for _ in range(n+1)]

queries = [[1,1,2,2],[0,0,1,1]]

for x1, y1, x2, y2 in queries:
    mat[x1][y1] += 1
    mat[x2 + 1][y1] -= 1
    mat[x1][y2 + 1] -= 1
    mat[x2 + 1][y2 + 1] += 1

for i in range(n):
    for j in range(n):
        mat[i][j] += mat[i][j-1] if j > 0 else 0

for i in range(n):
    for j in range(n):
        mat[i][j] += mat[i-1][j] if i > 0 else 0

print([row[:n] for row in mat[:n]])