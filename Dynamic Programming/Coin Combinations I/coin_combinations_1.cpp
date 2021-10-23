#include <bits/stdc++.h> 
using namespace std; 
int coin_combinations(int x, int * coins, int n){
    int mod = 1000000007;
    vector<int> dp(x+1,0);
    dp[0] = 1;
    for(int i = 1; i <=x ; i++){
        for(int j = 0; j < n; j++){
            if(i - coins[j] >= 0){
                (dp[i] += dp[i-coins[j]]) %= mod;
            }
        }
    } 
    return dp[x];
}
int minimizing_coins(int x, int * coins, int n){
    
    int mod = 1000000007;
    int * dp = new int[x+1];
    for(int i=0;i<=x;i++){
        dp[i] = 0;
    }
    dp[0] = 1;
 
    for(int i =1; i<=x;i++){
        if(dp[i] == 0){
            int count = 0;
            for(int j=0; j < n; j++){
                if(i - coins[j] >=0){
                    count += dp[i-coins[j]]%mod;
                }
            }
            dp[i] = count;
        }
    }
    
    return dp[x]%mod;
}
// int coin_combinations(int n, int x, int * coins, int ** dp){
//     if(x == 0){
//         return 1;
//     }
//     if(n == 0){
//         return 0;
//     }
//     if(x < 0){
//         return 0;
//     }
//     if(dp[x][n] != -1){
//         return dp[x][n];
//     }
//     int first = coin_combinations(n,x-coins[0],coins,dp);
//     int second = coin_combinations(n-1,x,coins + 1 ,dp);
//     dp[x][n] = first + second;
//     return dp[x][n];
// }
void solve(); 
int main() 
{ 
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
  
// #ifndef ONLINE_JUDGE 
//     freopen("input.txt", "r", stdin); 
//     freopen("error.txt", "w", stderr); 
//     freopen("output.txt", "w", stdout); 
// #endif 
  
    
    
        
            solve();
            cout << "\n";
        
         
    
    
  
    // cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl; 
    return 0; 
} 
void solve() 
{ 
    int n , x;
    cin >> n >> x;
    int * coins = new int[n];
    for(int i =0; i<n;i++){
        cin >> coins[i];
    }
    
    cout << coin_combinations(x,coins,n);
 
} 