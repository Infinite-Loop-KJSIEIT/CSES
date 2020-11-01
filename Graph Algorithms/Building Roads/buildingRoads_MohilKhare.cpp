/*
Author : Mohil Khare
Created On: 29 October 2020, 01:30
*/

#include <bits/stdc++.h>
#define ll long long int
#define vll vector<long long int>
#define vvll vector<vector<long long int>>
#define vpll vector<pair<long long int, long long int>>
#define mp make_pair
#define pb push_back
#define endl "\n"
#define here std::cout << "here\n";
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL);

// program specific shorts (if any)
const ll mod = 1000000007;
const ll MAX = 1e5+1;

using namespace std;

ll n, m;
vector<long long int> adj[MAX], ans;
bool vis[MAX];

void dfs(ll i) {
    vis[i] = true;
    for(auto x : adj[i])
        if(!vis[x])
            dfs(x);
}

int main() {
    fastIO;
    cin >> n >> m;
    memset(vis, false, sizeof(vis));
    for(ll i = 0; i < m; i++) {
        ll x, y; cin >> x >> y;
        adj[x].pb(y);
        adj[y].pb(x);
    }
    for(ll i = 1; i <= n; i++) {
        if(!vis[i]) {
            ans.pb(i);
            dfs(i);
        }
    }
    cout << ans.size()-1 << endl;
    for(ll i = 1; i < ans.size(); i++)
        cout << ans[0] << " " << ans[i] << endl;
    return 0;
}
