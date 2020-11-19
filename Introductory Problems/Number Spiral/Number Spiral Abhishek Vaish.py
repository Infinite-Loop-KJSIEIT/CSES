for _ in range(int(input())):
	r,c = map(int, input().split())
	if r > c:
		if r%2 == 0 :
			print((r-1)**2 + 2*r - c)
		else:
			print((r-1)**2 + c)
	else:
		if c%2==0:
			print((c-1)**2 + r)
		else:
			print((c-1)**2 + 2*c -r)