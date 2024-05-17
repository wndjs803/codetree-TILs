n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

count = [[0 for _ in range(n)] for _ in range(n)]
next_count = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    count[x-1][y-1] = 1

for i in range(n):
    for j in range(n):
        next_count[i][j] = count[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir_num = 0
change = True
# print(count)
while t:
    # print(t)
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 1:
                cur_num = arr[i][j]
                x, y = i, j
                for k in range(4):
                    nx = i + dx[dir_num+k]
                    ny = j + dy[dir_num+k]

                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if cur_num < arr[nx][ny]:
                            cur_num = arr[nx][ny]
                            x, y = nx, ny
                            
                next_count[x][y] += 1
                next_count[i][j] -= 1
                            

    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                next_count[i][j] = 0

    change = False
    for i in range(n):
        for j in range(n):
            if next_count[i][j] != count[i][j]:
                count[i][j] = next_count[i][j]
                change = True

    # print(count)
    
    t -= 1
    if change == False: 
        break

result = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            result += 1

print(result)