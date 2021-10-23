import sys
from typing import Sized
input=sys.stdin.readline
from heapq import heapify, heappush, heappop
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))

class DisjSet:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
        self.tot = n - 1

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def Union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if (a!=b):
            # print('tot', self.tot)
            self.tot -= 1
            # print('tot', self.tot)
            if self.size[a]<self.size[b]:
                self.parent[a] = b
                self.size[b] += self.size[a]
                return self.tot, self.size[b]
            else:    
                self.parent[b] = a
                self.size[a] += self.size[b]
                return self.tot, self.size[a]
        return self.tot,self.size[b]
 
  
n,m=I()
dsu=DisjSet(n+1)
largest= 1

for _ in range(m):
    x,y=I()
    tot, cur = dsu.Union(x,y)
    largest = max(largest,cur)
    print(tot,largest)
    # print(dsu.size)
    # print(dsu.parent)
    # print()
