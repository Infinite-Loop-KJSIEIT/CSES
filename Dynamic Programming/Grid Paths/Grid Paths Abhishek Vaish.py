n = int(input())
m = 1000000007
grid = [input() for i in range(n)]
if grid[0][0] == '*':
	print(0)
else :
	DP = [[0 for j in range(n)] for i in range(n) ]
	DP[n-1][n-1] = 1
	for i in reversed(range(n)):
		for j in reversed(range(n)):
			if i < n - 1:
				if grid[i+1][j] != '*':
					DP[i][j] = DP[i+1][j]%m
			if j < n - 1:
				if grid[i][j+1] != '*':
					DP[i][j] += DP[i][j+1]%m
	print(DP[0][0]%m)



