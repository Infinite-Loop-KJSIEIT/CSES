num1= int(input())
result1 = []
result2 = []
y=[]
# num1 should be greater than 3 
if num1 == 1 :
    print(num1)
elif num1 < 4 :
    print("NO SOLUTION")
else :
    if (num1 % 2 != 0):
        for i in range(1,num1+1,2): #num1 = 5
            result1.append(i)
        for i in result1:
            y = num1 - i
            result2.append(y)
        result2 = sorted(result2)
        y = (result1 + result2[1:]) 
        print(*y)
        #for even nos.
    else:
        for i in range(0,num1+1,2): #num1 = 6
            result1.append(i)
        for j in range(1,num1+1,2): #num1 = 6
            result2.append(j)    
        result2 = sorted(result2)
        y = (result1[1:] + result2)
        print(*y)