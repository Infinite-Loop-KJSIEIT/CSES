#include <bits/stdc++.h> 
using namespace std; 
int dice_combinations(int n){
   int mod = 1000000007;
   int * arr = new int[n+1];
   arr[0] = 0;
   arr[1] = 1;
   arr[2] = 2;
   arr[3] = 4;
   arr[4] = 8;
   arr[5] = 16;
   arr[6] = 32;
   if( n <= 6){
       return arr[n];
   }
   else{
       for(int i = 7; i <= n; i++){
           for(int j =1; j <=6; j++){
               arr[i] = (arr[i]%mod + arr[i-j]%mod)%mod;
           }
       }
       return arr[n];
   }
 
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
    int n;
    cin >> n;
    
    
    
    cout << dice_combinations(n);
}