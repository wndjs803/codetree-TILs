n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(t):
    temp1 = arr[0][n-1]
    temp2 = arr[1][n-1]

    for j in range(n-1, 0, -1):
        arr[0][j] = arr[0][j-1]
        arr[1][j] = arr[1][j-1]
    
    arr[0][0] = temp2
    arr[1][0] = temp1

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()