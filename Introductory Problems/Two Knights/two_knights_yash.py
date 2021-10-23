x = int(input())
for i in range(1,x+1):
    n = i * i
    total_ways = (n*(n-1))/2
    kills = (i-1)*(i-2)*2*2
    survived = total_ways - kills
    print(int(survived))