n = int(input())

mapper = {
    "W": 0,
    "S": 1,
    "N": 2,
    "E": 3
}

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

start_x, start_y = 0, 0
x, y = 0, 0

time = 0
for i in range(n):
    direction, step = input().split()

    for j in range(int(step)):
        x = x + dx[mapper[direction]]
        y = y + dy[mapper[direction]]

        time += 1

        if(x == start_x and y == start_y):
            print(time)
            break