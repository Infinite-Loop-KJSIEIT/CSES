from sys import stdin as stin, stdout

def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())

n = get_int()
x = sorted(get_list())
if n % 2 == 0:
    print(sum(x[n//2:])-sum(x[:n//2]))
else:
    print(sum(x[1+n//2:])-sum(x[:n//2]))
