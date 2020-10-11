#include <bits/stdc++.h>
 
using namespace std;
 
#define ar array
#define ll long long
 
const int MAX_N = 1e5 + 1;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const ll LINF = 1e18;
 
ll query(ll prefix[],int a,int b){
    if(a == 0) return prefix[b];
    else return prefix[b] - prefix[a-1];
}
 
void solve() {
    ll arr[200000], prefix[200000], ans;
    int a, b, n, q;
    cin >> n >> q;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    prefix[0] = arr[0];
    for(int i = 1; i < n;i++){
        prefix[i] = prefix[i-1] + arr[i];
    }
    for(int i = 0; i < q; i++){
        cin >> a >> b;
        cout << query(prefix,a-1,b-1) << endl;
    }
}
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
 
    solve();
}