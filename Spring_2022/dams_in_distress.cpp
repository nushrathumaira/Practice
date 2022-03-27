#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;
const int maxN = 2e6+1000;

int c[maxN], u_curr[maxN];
int dp[maxN];

vector<int> adj_list[maxN];


void dfs(int u)
{
   for(int v: adj_list[u])
   {
     dp[v] = max(dp[u],c[v]) - u_curr[v];
     dfs(v);
   }
}
int main(int argc,char *argv[])
{

    int n;
    ///srand(time(nullptr));
    ios_base::sync_with_stdio(0); 
    cin.tie(nullptr); 
    cout.tie(nullptr);
    cin >> n >> dp[0];
    for(int i =1; i <= n ; i++)
    {
        int u;
        cin >> u >> c[i] >> u_curr[i];
        adj_list[u].push_back(i);
    }
    dfs(0);
    cout << *min_element(dp,dp+n+1);
 }   