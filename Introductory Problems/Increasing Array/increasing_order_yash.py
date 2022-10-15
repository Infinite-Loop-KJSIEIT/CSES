t = int(input())
ls = [int(i) for i in input().split()]
count = 0 
for i in range(0,t-1):
    if ls[i] > ls[i+1]:
        count = count + (ls[i] - ls[i+1])
        ls[i+1] = ls[i]
print (count)        
        
    