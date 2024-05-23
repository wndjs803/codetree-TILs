# 기본 개념 j + a[j] >= i => j번째에서 a[j]만큼의 거리를 뛸 수 있는데 그게 i번째보다는 커야 한다. 

n = int(input())
arr = list(map(int, input().split()))

dp = [-1] * n

dp[0] = 1

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == -1:
            continue
        
        if arr[j] <= arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))