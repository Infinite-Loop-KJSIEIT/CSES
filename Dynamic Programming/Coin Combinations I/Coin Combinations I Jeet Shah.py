from sys import stdin as stin, stdout as stout

def get_ints(): return map(int, stin.readline().split())
def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()

n, x = get_ints()
deno = get_list()
deno.sort()
arr = [1] + [0] * (x)
for i in range(1, x + 1):
    for j in range(n):
        if i - deno[j] >= 0:
            arr[i] = (arr[i] + arr[i - deno[j]]) % (10 ** 9 + 7)
        else:
            break
print(arr[-1])
