from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if visited[nx][ny] == False and graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    step[nx][ny] = step[x][y] + 1

bfs()

if step[n-1][m-1] != 0:
    print(step[n-1][m-1])
else: print(-1)