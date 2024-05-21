from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

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

bfs()

if visited[n-1][m-1]:
    print(1)
else: print(0)