"""
https://cses.fi/problemset/task/1621
You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
"""
 
def solve():
    x.sort()
    count = 1
    for i in range(1,n):
        if x[i-1] != x[i]:
            count += 1
    print(count)
 
if __name__ == '__main__':
    n = int(input())
    x = list(map(int,input().split()))
    solve()
    