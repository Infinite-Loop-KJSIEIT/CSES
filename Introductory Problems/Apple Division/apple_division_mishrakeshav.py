def helper(current,total,i,arr):
    if(i == len(arr)):
        return abs(total - 2*current)
    
    a1 =  helper(current + arr[i], total , i + 1, arr)
    a2 = helper(current,total, i + 1, arr)
    return min(a1,a2)

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    total = sum(arr)
    ans = helper(0,total,0,arr)
    print(ans)


if __name__ == '__main__':
    solve()