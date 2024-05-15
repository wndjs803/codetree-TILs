n, r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
r = r - 1
c = c - 1
check = False

print(arr[r][c], end=' ')

for i in range(n):
    for j in range(n):
        dir_num = 0
        cur_num = arr[r][c]

        for k in range(4):
            nc = c + dc[dir_num+k]
            nr = r + dr[dir_num+k]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if arr[nr][nc] > cur_num:
                    r, c = nr, nc
                    print(arr[r][c], end=' ')
                    break

            if nr == r and nc == c:
                check = True
                break

        if check: break
    if check: break