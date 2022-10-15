# import numpy as np
# import decimal as dec
# import itertools as it
# import collections as coll
# import random as rd
# import bisect as bi
# import functools as ft
# from heapq import heapify, heappop, heappush
import time
import sys

sys.setrecursionlimit(1000000)
mod = 1000000007


def uno():
	return int(sys.stdin.readline().strip())


def dos():
	return sys.stdin.readline().strip()


def tres():
	return map(int, sys.stdin.readline().strip().split())


def cuatro():
	return sys.stdin.readline().strip().split()


# Starting Time
time1 = time.time()


######## ? CODE STARTS FROM HERE ########
n = uno()
if 1 < n < 4:
    print("NO SOLUTION")
else:
	for i in range(2, n + 1, 2):
		print(i, end=" ")
	for i in range(1, n + 1, 2):
		print(i, end=" ")

# End Time
time2 = time.time()
time = (
	str(round((time2 - time1) * 1000, 3)) + "ms"
	if (round((time2 - time1) * 1000, 3)) < 1000
	else str(round(time2 - time1, 3)) + "s"
)
# print("\nTime Taken:", time)
