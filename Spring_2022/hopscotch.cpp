#include <cstdio>
#include<vector>
#include<algorithm>
#include<iostream>

typedeflonglong ll;
using namespace std;

ll mod = 1000000007;
const int maxn = 1000010;

ll qpow(ll a, ll x)
{
  ll ret = 1;
  while(x)
  {
      if(x&1)
        ret = ret * a %mod;
      a = a*a % mod;
      x >>=1;
  }
  return ret;
}

ll fac[maxn],inv[maxn];

ll init()
{
  fac[0]=1;
  for(int i =1; i <maxn; i++)
  {
    fac[i] = fac[i-1]*i % mod;
  }
  inv[maxn-1] = qpow(fac[maxn-1],mod-2);
  for(int i = maxn-2; i>=0;i--)
  {
    inv[i] = inv[i+1]*(i+1)%mod;
  }
  return 0;
}
ll combination(ll n, ll m)
{
   if (n<m) return 0;
   return fac[n]* inv[m]%mod*inv[n-m]%mod;
}

ll dp1[maxn], dp2[maxn];
int main()
{
  init();
  ll n,x,y;
  scanf("%lld%lld%lld",&n,&x,&y);
  for(int i =1; i*x <= n; i++)
  {
    dp1[i] = combination(n-(x-1)*i-1, i-1);
  }
  for(int i =1; i *y <=n ; i++)
  {
    dp2[i] = combination(n-(y-1)*i-1,i-1);
  }
  ll ans = 0;
  for(int i = 1; i*x <=n && i*y<=n; i++)
  {
     ans = (ans + dp1[i] * dp2[i]%mod)%mod;
  }
   printf("%lld\n",ans);



  return 0;
}