#include <bits/stdc++.h>
#include <bits/extc++.h>
 
#define all(x) (x).begin(), (x).end()
#define fr(i, a, n) for (int i = (a); i < (n); i++)
#define frb(i, n, a) for (int i = (n)-1; i >= (a); i--)
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
 
template <class T>
using Tree = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin.exceptions(cin.failbit);
 
    ll n, k;
    cin >> n >> k;
    vl a(n);
    fr(i, 0, n) cin >> a[i];
    Tree<pll> t;
    fr(i, 0, n)
    {
        t.insert({a[i], i});
        if (i >= k)
            t.erase({a[i - k], i - k});
        if (i >= k - 1)
            cout << t.find_by_order((k - 1) / 2)->ft << sp;
    }
 
    return 0;
}
