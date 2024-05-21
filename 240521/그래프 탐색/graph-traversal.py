n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

root_vertex = 1

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

visited[root_vertex] = True
dfs(root_vertex)

count = sum(1 for x in visited if x is True)
print(count-1)