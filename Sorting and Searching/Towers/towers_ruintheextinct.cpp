#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
 
#define all(x) (x).begin(), (x).end()
#define fr(i, a, n) for (int i = (a); i < (n); i++)
#define frd(i, a, n) for (int i = (n)-1; i >= (a); i--)
#define sz(x) (int)(x).size()
#define trav(a, x) for (auto &a : x)
 
#define str string
#define ll long int
#define li unsigned long int
#define vll long long int
#define vli unsigned long long int
#define pll pair<ll, ll>
#define vl vector<ll>
#define vpl vector<pl>
 
#define ft first
#define sc second
#define mp make_pair
#define pb push_back
#define lb lower_bound
 
#define ed "\n"
#define sp " "
 
#define N 100005
#define MOD 1000000007
 
//#define ONLINE_JUDGE 1
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
 
    ll n, ans = 1, l, r, m, z;
    cin >> n;
    vl k;
    fr(i, 0, n)
    {
        cin >> z;
        l = 0;
        r = sz(k);
        while (l < r)
        {
            m = (l + r) / 2;
            if (k[m] > z)
                r = m;
            else
                l = m + 1;
        }
        if (l == sz(k))
            k.pb(z);
        else
            k[l] = z;
    }
    cout << sz(k) << ed;
    return 0;
}
