n,m,k = map(int, input().split())
applicants =  sorted(list(map(int, input().split())))
apartments = sorted(list(map(int, input().split())))
i,j,count = 0,0,0
while i < m and j < n:
	if abs(applicants[j] - apartments[i]) <= k:
		count += 1
		j+=1
		i+=1
	elif applicants[j] > apartments[i] :
		i += 1
	else :
		j += 1
print(count)