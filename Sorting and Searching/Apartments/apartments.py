def solve():
    i = 0 
    j = 0 
    count = 0
    while i < n and j < m:
        if (b[j] - k <= a[i] <= b[j] + k):
            count += 1
            i += 1 
            j += 1
        elif a[i] < b[j] - k:
            i += 1
        elif a[i] > b[j] + k:
            j += 1
    print(count)
        
 
 
if __name__ == '__main__':
    n, m, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()
    a.sort()
    solve()