def wierd_algo(n):
    if n%2==0:
        n /= 2
        ans.append(int(n))        
    else:
        n = n*3 + 1
        ans.append(int(n))   
    return ans
 
if __name__ == "__main__":
    ans = []
    n = int(input())
    wierd_algo(n)
    if n==1:
        print(1)
    else:
        while(ans[-1]!=1):
            wierd_algo(ans[-1])
        print(n,*ans)