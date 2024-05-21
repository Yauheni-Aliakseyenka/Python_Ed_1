n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
x, y = 0, 0
dx, dy = 0, 1

for i in range(1, n ** 2 + 1):
    matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and not matrix[nx][ny]:
        x, y = nx, ny
    else:
        dy, dx = -dx, dy
        x, y = x + dx, y + dy

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

