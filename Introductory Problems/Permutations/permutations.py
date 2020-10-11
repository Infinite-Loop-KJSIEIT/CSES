def solve():
    n = int(input())
    if n == 1:
        print(n, end = " ")
    elif n <= 3:
        print("NO SOLUTION", end = " ")
    elif n == 4:
        print("2 4 1 3", end = " ")
    else:
        for i in range(1,n+1,2):
            print(i, end = " ")
        for i in range(2,n+1,2):
            print(i, end = " ")
if __name__ == '__main__':
    
    solve()
        