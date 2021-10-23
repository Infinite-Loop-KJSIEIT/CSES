def solve():
    p.sort()
    i = 0 
    j = n - 1
    count = 0
    while i < j:
        if p[i] + p[j] <= x:
            count += 1
            i += 1  
            j -= 1
        else:
            count += 1 
            j -= 1         
        if i == j:
            count += 1 
            break
        
    
    print(count)
        
 
 
 
 
if __name__ == '__main__':
    n, x = map(int,input().split())
    p = list(map(int,input().split()))
    solve()