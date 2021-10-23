n = int(input())
mod = 10 ** 9 + 7
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if i <= 6:
        for j in range(1, 7):
            if j > i:
                break
            dp[i] = (dp[i] + dp[i - j]) % mod
    else:
        dp[i] += sum(dp[i - 6:i]) % mod
print(dp[n] % (10 ** 9 + 7))
