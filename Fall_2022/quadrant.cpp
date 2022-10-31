#include <bits/stdc++.h>

int main()
{
    int x, y;
    int ans = 0;
    std::cin >> x >> y ;
    ans = (x < 0) ? ((y< 0) ? 3 : 2) : ((y < 0) ? 4 : 1);
    std::cout << ans;
    return 0;
}