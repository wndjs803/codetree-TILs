n = int(input())

# arr = [list(map(int, input().split())) for_ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + arr[i][j], dp[i][j-1] + arr[i][j])

print(dp[n-1][n-1])