n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

total = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx >= 0 and nx < len(arr) and ny >= 0 and ny < len(arr[i]):
                if arr[nx][ny] == 1:
                    cnt += 1
        if cnt >= 3:
            total += 1
print(total)