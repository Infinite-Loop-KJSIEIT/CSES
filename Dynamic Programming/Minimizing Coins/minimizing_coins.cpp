#include <bits/stdc++.h> 
using namespace std; 
int minimizing_coins1(int x, int * coins, int n){
    vector<int> dp(x+1,1e9);
    dp[0] = 0;
    for(int i =1; i <=x ; i++){
        for(int j=0; j < n; j++){
            if(i-coins[j] >=0){
                dp[i] = min(dp[i], dp[i-coins[j]] + 1);
            }
        }
    }
    return dp[x] == 1e9 ? -1 : dp[x];
}
int minimizing_coins(int x, int * coins, int n){
    int flag = 1;
    for(int i = 0; i< n; i++){
        if(coins[i] == x){
            return 1;
        }
        if(coins[i] < x){
            flag = 0;
        }
    }
    if(flag){
        return -1;
    }
    int * dp = new int[x+1];
    for(int i=0;i<=x;i++){
        dp[i] = INT_MAX;
    }
    dp[0] = 0;
    for(int i =0; i< n; i++){
        dp[coins[i]] = 1;
    }
    for(int i =1; i<=x;i++){
        if(dp[i] == INT_MAX){
            int count = INT_MAX;
            for(int j=0; j < n; j++){
                if(i - coins[j] >=0){
                    count = min(count,dp[i-coins[j]] + 1);
                }
            }
            dp[i] = count;
        }
    }
    if(dp[x] == INT_MAX) return -1;
    return dp[x];
}
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
    int n,x;
    cin >> n >> x;
    int * coins = new int[n];
    for(int i=0; i< n;i++){
        cin >> coins[i];
    }
    cout << minimizing_coins1(x,coins,n);
    
} 