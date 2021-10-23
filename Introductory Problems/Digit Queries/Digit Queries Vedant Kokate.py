import math

q=int(input())
for Q in range(q):
    k=int(input())

    digit=1
    while k-9*(10**(digit-1))*digit>0:
        k-=9*(10**(digit-1))*digit      
        digit+=1

    if digit>1:

        num=math.ceil(int('9'*(digit-1))+k//digit)
        if k%digit!=0:
            num+=1

        place=(k%digit)-1

        print(str(num)[place])
    else:
        print(k)
    
    
    