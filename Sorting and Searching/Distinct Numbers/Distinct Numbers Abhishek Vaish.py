n = int(input())
numbers = list(map(int,input().split()))
memo = {}
for n in numbers:
	if not memo.get(n):
		memo[n] = 1
print(len(memo.keys()))