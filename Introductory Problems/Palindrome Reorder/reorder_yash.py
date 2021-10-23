x = input()   #AABBCC
list1 = sorted(list(set(x)))
result = ""
y= 0   
m = ''
for i in list1:
    n = (x.count(i))
    if n % 2 == 0:
        result += i * (n//2)
    elif y == 1 :
        result = ""
        print("NO SOLUTION")
        break
    elif n % 2 != 0:
        y = 1     # for odd nos.
        m = i     # ek idhar gaya baki ke neeche
        result += i * ((n-1)//2)       
if result != "":     
    print(result + m + result[::-1]) 
else : 
    print (m) 