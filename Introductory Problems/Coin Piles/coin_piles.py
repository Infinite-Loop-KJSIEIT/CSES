"""
Problem link:
"""
from sys import stdin,stdout
def input(): return stdin.readline().strip()
# def print(s): stdout.write(str(s)+'\n')
 
 
def solve():
    a, b = map(int,input().split())
    if (a > 2*b) or (b > 2*a):
        print('NO')
    else:
        if (a+b)%3 == 0:
            print('YES')
        else:
            print('NO')
 
 
if __name__ == '__main__':
    for t in range(int(input())):
        solve()