#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>
 
#define all(x) (x).begin(), (x).end()
#define fr(i, a, n) for (int i = (a); i < (n); i++)
#define frb(i, a, n) for (int i = (n)-1; i >= (a); i--)
#define sz(x) (int)(x).size()
#define trav(a, x) for (auto &a : x)
 
#define str string
#define li long int
#define uli unsigned long int
#define ll long long
#define ull unsigned long long
#define pll pair<ll, ll>
#define vl vector<ll>
#define vpl vector<pll>
#define ml multiset<ll>
 
#define ft first
#define sc second
#define mp make_pair
#define pb push_back
#define lb lower_bound
 
#define ed '\n'
#define sp ' '
 
#define N 200005
#define MOD 1000000007 // 998244353
 
/*
    g++ cses.cpp -o cses.exe
    g++ -o cses cses.cpp&cses.exe
*/
 
using namespace std;
using namespace __gnu_pbds;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin.exceptions(cin.failbit);
 
    ll n, a, d, ans = 0, s = 0;
    cin >> n;
    vl t(n);
    fr(i, 0, n) cin >> t[i];
    s = accumulate(all(t), 0LL);
    ans = *max_element(all(t));
    cout << max(s, 2 * ans);
 
    return 0;
}
