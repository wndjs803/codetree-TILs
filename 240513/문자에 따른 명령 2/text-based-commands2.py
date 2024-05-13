commands = input()
direction = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for command in commands:
    if command == "L":
        direction = (direction -1 + 4) % 4
    elif command == "R":
        direction = (direction + 1) % 4
    else:
        x, y = x + dx[direction], y + dy[direction]

print(x, y)