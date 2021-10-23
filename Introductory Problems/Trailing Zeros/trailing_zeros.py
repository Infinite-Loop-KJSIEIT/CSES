"""
Your task is to calculate the number of trailing zeros in the factorial n!.
 
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
"""
def solve(n):
    i = 5 
    count = 0 
    while n//i >= 1:
        count += n//i
        i *= 5 
 
    print(count)
     
 
 
if __name__ == '__main__':
    n = int(input())
    solve(n)
