m = int(input())
for n in range(1, m+1):
    kill_ways = (n - 1) * (n - 2) * 2 * 2
    total_ways = (n ** 2) * ((n ** 2) - 1) // 2
    print(total_ways-kill_ways)
