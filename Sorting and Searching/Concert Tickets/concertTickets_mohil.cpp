/*
Author : Mohil Khare
Created On: 17 September 2020, 15:09
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
    ll n, m, ele; cin >> n >> m;
    multiset<ll, greater<ll>> tix;
    ll ppl[m];
    for(ll i = 0; i < n; i++) {cin >> ele; tix.insert(ele);}
    for(ll i = 0; i < m; i++) cin >> ppl[i];
    //for(auto x : tix) cout << x << " "; cout << endl;
    for(ll i = 0; i < m; i++) {
        cout << *tix.lower_bound(ppl[i]) << endl;
        if(tix.lower_bound(ppl[i]) == tix.end());// cout << "-1" << endl;
        else {
            //cout << *tix.lower_bound(ppl[i]) << endl;
            tix.erase(tix.lower_bound(ppl[i]));
        }
    }
    return 0;
}
