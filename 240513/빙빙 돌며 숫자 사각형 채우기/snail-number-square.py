n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = [[0 for _ in range(m)] for _ in range(n)]

arr[0][0] = 1

x, y = 0, 0
dir_num = 0

for i in range(2, n * m + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not(0<=nx<m and 0<=ny<n) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x = x + dx[dir_num]
    y = y + dy[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()