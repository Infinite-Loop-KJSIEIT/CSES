#import time
#import bisect
#import math
import sys
#import random as r
from collections import deque
#from collections import defaultdict 
#from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
 

 
n, m = get_ints()
M = [list(inp_str()) for _ in range(n)]
D = ((1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L'))
Q = deque([(X, Y) for X in range(n) for Y in range(m) if M[X][Y] == 'A'])
while Q:
	x, y = Q.popleft()
	for a, b, c in D:
		A = x + a
		B = y + b
		if 0 <= A < n and 0 <= B < m:
			R = M[A][B]
			if R == '.':
				M[A][B] = (x, y, c)
				Q.append((A, B))
			elif R == 'B':
				print('YES')
				p = [c]
				while M[x][y] != 'A':
					x, y, c = M[x][y]
					p.append(c)
				print(len(p))
				print(''.join(p[::-1]))
				raise SystemExit
print('NO')
     
