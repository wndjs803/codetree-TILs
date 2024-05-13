n = int(input())

x, y = 0, 0

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(n):
    direction, step = input().split()

    if direction == "W":
        for j in range(int(step)):
            x, y = x + dx[2], y + dy[2]
    elif direction == "S":
        for j in range(int(step)):
            x, y = x + dx[1], y + dy[1]
    elif direction == "N":
        for j in range(int(step)):
            x, y = x + dx[3], y + dy[3]
    elif direction == "E":
        for j in range(int(step)):
            x, y = x + dx[0], y + dy[0]

print(x, y)