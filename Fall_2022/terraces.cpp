#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long ull;


int n, m;

int flatten(int i, int j) {
    return i*n+j;
}
int find(vector<int>& d, int a) {
    if(d[a] == -1) {
        return a;
    }
    return d[a] = find(d, d[a]);
}
void join(vector<int>& d, int a, int b) {
    a = find(d, a);
    b = find(d, b);
    if(a == b) return;
    d[a] = b;
}
int main() {

    cin >> n >> m;

    vector<vector<int>> v;
    v.resize(m, vector<int>(n));

    for(auto& i : v) {
        for(auto& j : i) {
            cin >> j;
        }
    }
    vector<bool> visited(n*m, true);
    vector<int> d(n*m, -1);
        for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(i > 0) {
                if(v[i][j] == v[i-1][j]) {
                    join(d, flatten(i,j), flatten(i-1,j));
                }
                else if(v[i][j] < v[i-1][j]) {
                    visited[flatten(i-1,j)] = false;
                }
                else {
                    visited[flatten(i,j)] = false;
                }
            }
            if(j > 0) {
                if(v[i][j] == v[i][j-1]) {
                    join(d, flatten(i,j), flatten(i,j-1));
                }
                else if(v[i][j] < v[i][j-1]) {
                    visited[flatten(i,j-1)] = false;
                }
                else {
                    visited[flatten(i,j)] = false;
                }
            }
        }
    }
    
    for(int i = 0; i < n*m; i++) {
        int here = find(d, i);
        if(!visited[i]) {
            visited[here] = false;
        }
    }

    int cc_count = 0;
    for(int i = 0; i < n*m; i++) {
        int here = find(d, i);
        if(visited[here]) {
            cc_count++;
        }
    }

    cout << cc_count << endl;

    return 0;
}
