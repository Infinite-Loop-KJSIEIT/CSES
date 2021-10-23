ans = set()

def permutation(s,prefix):
    if len(s) == 0:
        ans.add(prefix)
    elif len(s) == 1:
        ans.add(s + prefix)
    elif len(s) == 2:
        ans.add(s[-2] + s[-1] + prefix)
        ans.add(s[-1] + s[-2] + prefix)
    else:
        n = len(s)
        for i in range(n):
            permutation(s[:i] + s[i+1:], s[i] + prefix)

def solve():
    global ans 
    s = input()
    n = len(s)
    permutation(s,"")
    print(len(ans))
    ans = list(ans)
    ans.sort()
    for st in ans:
        print(st)
if __name__ == '__main__':
    
    solve()