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
#define ll long int
#define li unsigned long int
#define vll long long int
#define vli unsigned long long int
#define pll pair<ll, ll>
#define vl vector<ll>
#define vpl vector<pll>
#define ml multiset<ll>

#define ft first
#define sc second
#define mp make_pair
#define pb push_back
#define lb lower_bound

#define ed "\n"
#define sp " "

#define N 100005
#define MOD 1000000007

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
    cout.tie(NULL);

    ll n, a, b, i, ans = 0;
    vpl rm;
    cin >> n;
    fr(i, 1, n + 1)
    {
        cin >> a >> b;
        rm.pb({a, i});
        rm.pb({b + 1, -i});
    }
    sort(all(rm));
    vl p, q(n + 1);
    trav(x, rm)
    {
        i = x.sc;
        if (i > 0)
        {
            if (sz(p))
            {
                q[i] = p.back();
                p.pop_back();
            }
            else
            {
                q[i] = ++ans;
            }
        }
        else
        {
            p.pb(q[-i]);
        }
    }
    cout << ans << ed;
    fr(i, 1, n + 1)
    {
        cout << q[i] << sp;
    }

    return 0;
}