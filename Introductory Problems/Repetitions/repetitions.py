def solve():
    s = input()
    mx = 0 
    count = 1
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            count += 1 
        else:
            mx = max(count,mx)
            count = 1 
    mx = max(count,mx)        
    print(mx)
                
 
if __name__ == '__main__':
    solve()