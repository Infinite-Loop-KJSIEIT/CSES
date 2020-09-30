/*
Author : Mohil Khare
Created On: 29 September 2020, 17:55
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

using namespace std;

int main() {
    fastIO;
    ll n, m, k; cin >> n >> m >> k;
    ll a[n], b[m];
    for(ll i = 0; i < n; i++) cin >> a[i];
    for(ll j = 0; j < m; j++) cin >> b[j];
    sort(a, a+n);
    sort(b, b+m);
    ll x = 0, y = 0, got = 0;
    while(x < n && y < m) {
        if(abs(a[x] - b[y]) <= k)
            got++, x++, y++;
        else
            (a[x] > b[y]) ? y++ : x++; 
    }
    cout << got;
    return 0;
}