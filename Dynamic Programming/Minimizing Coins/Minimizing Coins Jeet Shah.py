def solve():
    n, s = map(int, input().split())
    deno = list(map(int, input().split()))
    deno.sort()
    arr = [float("inf")] * (s + 1)
    arr[0] = 0
    for i in range(s + 1):
        for j in deno:
            if i-j >= 0:
                arr[i] = min(1 + arr[i - j], arr[i])
            else:
                break

    if arr[s] == float("inf"):
        print(-1)
        return
    print(arr[s])


if __name__ == "__main__":
    solve()
