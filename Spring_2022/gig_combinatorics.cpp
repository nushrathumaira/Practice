#include <iostream>

using namespace std;

int main() {
    // fast io
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    constexpr int mod = 1e9 + 7;
    int count1 = 0;
    int count12 = 0;
    int res = 0;
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int cur;
        cin >> cur;
        if (cur == 1) {
            ++count1;
        } else if (cur == 2) {
            count12 = (count12 * 2 + count1) % mod;
        } else {
            res = (res + count12) % mod;
        }
    }
    cout << res;
}