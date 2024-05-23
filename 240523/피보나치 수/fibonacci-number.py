n = int(input())

dp = [0] * (n + 1)

# dp[1] = 1

# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]

def fibbo(n):
    if dp[n] != 0:
        return dp[n]
    
    if n <= 2:
        dp[n] = 1
    else:
        dp[n] = fibbo(n -1) + fibbo(n-2)

fibbo(n)
print(dp[n])