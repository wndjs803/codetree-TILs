n = int(input())

x, y = 0, 0

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(n):
    direction, step = input().split()

    if direction == "W":
        x, y = x + dx[2]*int(step), y + dy[2]
    elif direction == "S":
        x, y = x + dx[1], y + dy[1]*int(step)
    elif direction == "N":
        x, y = x + dx[3], y + dy[3]*int(step)
    elif direction == "E":
        x, y = x + dx[0]*int(step), y + dy[0]

print(x, y)