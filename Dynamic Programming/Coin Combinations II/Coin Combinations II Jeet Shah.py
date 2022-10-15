from sys import stdin as stin, stdout as stout, setrecursionlimit as srl

n, x = map(int, stin.readline().split())
deno = list(map(int, stin.readline().split()))
arr = [1] + [0] * x

for j in range(n):
    for i in range(deno[j], x + 1):
        arr[i] = (arr[i] + arr[i - deno[j]]) % (10 ** 9 + 7)

print(arr[x])
