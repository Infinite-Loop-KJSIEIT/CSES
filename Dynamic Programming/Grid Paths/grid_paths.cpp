#include <bits/stdc++.h> 
#include <string.h> 
using namespace std; 
int mod = 1e9 + 7;
 
int main(){
    int n;
    cin >>n;
    char ** grid = new char*[n];
    for(int i=0; i<n; i++){
        grid[i] = new char[n];
    }
    for(int i =0; i < n; i++){
        for(int j=0; j < n; j++){
            cin >> grid[i][j];
        }
    }
    int dp[n][n];
    memset(dp,0,sizeof(dp));
    if(grid[n-1][n-1] != '*'){
        dp[n-1][n-1] = 1;
    }
    for(int i = n-2; i >= 0; i--){
        if(grid[i][n-1] != '*'){
            (dp[i][n-1] += dp[i+1][n-1])%=mod ;
        }
    }
    for(int i = n-2; i >= 0; i--){
        if(grid[n-1][i] != '*'){
            (dp[n-1][i] = dp[n-1][i+1])%=mod;
        }
    }
    for(int i=n-2; i >=0; i--){
        for(int j=n-2; j>=0; j--){
            if(grid[i][j] != '*'){
                dp[i][j] = (dp[i+1][j]+ dp[i][j+1])%mod;
            }
        }
    }
    // cout << "\n";
    // for(int i=0; i<n; i++){
    //     for(int j=0; j<n; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    // if(dp[n-1][n-1] == '*'){
    //     dp[0][0] = 0;
    // }
    cout << dp[0][0] << endl;
    
    return 0;
}