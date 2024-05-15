cmds = input()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

start_x = 0
start_y = 0

x, y = 0, 0
time = 0
dir_num = 0
check = False

for cmd in cmds:
    if cmd == "L":
        dir_num = (dir_num -1 + 4) % 4
    elif cmd == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]
    
    time += 1

    if x == start_x and y == start_y:
        check = True
        break

if check:
    print(time)
else: print(-1)