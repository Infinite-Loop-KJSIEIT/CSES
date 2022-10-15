from sys import stdin as stin, stdout as stout

def get_ints(): return map(int, stin.readline().split())
def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()

n, x = get_ints()
a = get_list()

def solve1():
    temp = {}
    for i in range(n):
        p = a[i]
        if x - p in temp:
            print(i+1, temp[x-p]+1)
            return True
        else:
            temp[p] = i
    print("IMPOSSIBLE")
    return False

solve1()