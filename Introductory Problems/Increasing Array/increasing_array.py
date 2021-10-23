def solve():
    n = int(input())
    x = list(map(int,input().split()))
    count = 0
    for i in range(1,n):
        if x[i-1] > x[i]:
            count += x[i-1] - x[i]
            x[i] += x[i-1] - x[i]
    print(count)
 
 
if __name__ == '__main__':
    solve()