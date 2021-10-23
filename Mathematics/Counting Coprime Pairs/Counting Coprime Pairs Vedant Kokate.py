N = 10**6+1
lpf = [0 for i in range(N)]
mobius = [0 for i in range(N)]

def least_prime_factor():
	for i in range(2, N):	
		if (lpf[i] == 0):
			for j in range(i, N, i):
				if (lpf[j] == 0):
					lpf[j] = i

def Mobius():
	for i in range(1, N):
		if (i == 1):
			mobius[i] = 1
		else:
			if (lpf[ (i // lpf[i]) ] == lpf[i]):
				mobius[i] = 0
			else:
				mobius[i] = -1 * mobius[i // lpf[i]]

def gcd_pairs(a, n):
	maxi = 0
	fre = [0 for i in range(N)]
	for i in range(n):
		fre[a[i]] += 1
		maxi = max(a[i], maxi)
	least_prime_factor()
	Mobius()
	ans = 0
	for i in range(1, maxi + 1):
		if (mobius[i] == 0):
			continue
		temp = 0
		for j in range(i, maxi + 1, i):
			temp += fre[j]
		ans += temp * (temp - 1) // 2 * mobius[i]
	return ans
    
n=int(input())
a = list(map(int,input().split()))
print(gcd_pairs(a, n))

