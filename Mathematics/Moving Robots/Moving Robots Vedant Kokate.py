import sys 
input=sys.stdin.readline
n=int(input())
ans = [[1] * 8 for _ in range(8)]
 
for i2 in range(8):
    for j2 in range(8):
        dp = [[0] * 8 for _ in range(8)]
        dp[i2][j2] = 1
        for _ in range(n):
            dp2 = [[0] * 8 for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    d=0
                    for x, y in (0, 1), (1, 0), (-1, 0), (0, -1):
                        if 0 <= x + i < 8 and 0 <= y + j < 8:
                            d+=1
                    for x, y in (0, 1), (1, 0), (-1, 0), (0, -1):
                        if 0 <= x + i < 8 and 0 <= y + j < 8:
                            dp2[x + i][y + j] += dp[i][j] /d
                        
            dp = dp2
        for i in range(8):
            for j in range(8):
                ans[i][j] *= 1 - dp[i][j]
 
print(f"{sum(sum(ans, [])):.6f}")