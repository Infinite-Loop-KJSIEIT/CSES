def calc(n):
    # total number of ways two knights can be placed 
    total = (n**2)*(n**2-1)//2
    # total number of ways two knights can attack each other 
    attack = 4*(n-1)*(n-2)
    return total-attack

def solve():
    n = int(input())
    
    for i in range(1,n+1):
        print(calc(i))


if __name__ == '__main__':
    solve()