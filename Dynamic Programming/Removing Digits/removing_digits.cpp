#include <bits/stdc++.h> 
#include <string.h> 
using namespace std; 
int mod = 1e9 + 6;
int removing_digits(int n){
    
    int j;
    if(n == 0){
        return 0;
    }
    if(n < 0 ){
        return 1;
    }
    int dp[n + 1];
    for(int i =0; i<= n; i++){
        dp[i] = mod;
    }
    dp[0] = 0;
    for(int i = 1; i <= 9; i++){
        dp[i] = 1;
    }
    for(int i = 10; i <= n; i++){
        j = i;
        while(j){
            dp[i] = min(dp[i- j%10] + 1, dp[i]);
            j = j/10;
        }
    }
    
    return dp[n];
}
int main(){
    int n;
    cin >>n;
    int ans = removing_digits(n);
    cout << ans << endl;
    return 0;
}