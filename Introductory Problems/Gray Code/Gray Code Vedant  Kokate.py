n=int(input())
for i in range((1<<n)):
    #print(i^(i>>1))
    x=bin(i^(i>>1)).replace("0b","")
    x=(n-len(x))*"0"+x
    print(x)
