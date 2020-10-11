if __name__ == '__main__':
    n = int(input())
    numbers = [None]*(n+1)
    a = list(map(int,input().split()))
    for i in a:
        numbers[i] = True 
   
    for i in range(1,n+1):
        if numbers[i] is None:
            print(i)