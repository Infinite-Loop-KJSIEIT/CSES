
def solve():
    n = int(input())
    k = list(map(int,input().split()))
    hashmap = dict()
    j = 0
    ans = 0 
    c = 0  
    for i in range(n):
        if k[i] in hashmap and hashmap[k[i]] > 0:
            while i > j and k[i] in hashmap and hashmap[k[i]] > 0:
                hashmap[k[j]] -= 1 
                j += 1 
                c -= 1 
        hashmap[k[i]] = 1 
        c += 1 
        ans = max(ans,c)
    print(ans)




if __name__ == '__main__':
    solve()