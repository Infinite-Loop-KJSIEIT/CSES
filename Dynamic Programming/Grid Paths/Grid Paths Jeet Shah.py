from sys import stdin as stin, stdout as stout
def get_list(): return list(stin.readline())[:-1]


def solve():
    n = int(input())
    mod = 10**9+7
    arr = []
    for _ in range(n):
        arr.append(get_list())

    if arr[0][0] == '*' or arr[-1][-1] == '*':
        return 0
    else:
        dp = [[0 for k in range(n+1)]for p in range(n+1)]
        dp[1][1] = 1
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    pass
                elif arr[i][j] == '*':
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1]) % mod
        return(dp[-1][-1])


if __name__ == "__main__":
    print(solve())
