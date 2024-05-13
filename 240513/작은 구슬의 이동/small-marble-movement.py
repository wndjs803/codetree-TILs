n, t = map(int, input().split())
x, y, d = input().split()

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

mapper = {
    "U" : 2,
    "D" : 1,
    "R" : 0,
    "L" : 3
}

direction = mapper[d]

x = int(x)
y = int(y)

for i in range(t):
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if nx > 0 and nx <= n and ny > 0 and ny <= n:
        x, y = nx, ny
    else:
        direction = 3 - direction


print(x, y)