def solve():
    a, b = map(int,input().split())
    m = max(a,b)
    print(m*(m-1) + 1 + ((-1)**m)*(a-b)) 
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()