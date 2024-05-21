n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [1, 0]
dy = [0, 1]
check = 0

def dfs(x, y):
    global check
    if x == n -1 and y == m - 1:
        check = 1
        return
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < 5 and ny >= 0 and ny < m:
            if visited[nx][ny] == False and graph[x][y] == 1:
                x, y = nx, ny
                visited[x][y] = True
                dfs(x, y)

print(check)