n = int(input())
a = [0]*(n+1)
a[1] = 1
for i in range(2,n+1):
	if i < 7:sum_= 1
	else:sum_= 0
	for k in range(1,min(n,7)):
		sum_ += a[i-k]
		sum_ %= 1000000007
	a[i] = sum_
print(a[n])