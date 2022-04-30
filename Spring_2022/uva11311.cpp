//exclusively edible

#include <iostream>

using namespace std;


int main(void)
{
  int t, h, w, x, y;
  int start_row, start_col, nim = 0;
  cin >> t;
  while(t--)
  {
      cin >> h >> w >> x >> y;
      start_row = h - x -1;
      start_col = w - y -1;
      nim = x ^ start_row ^ y ^ start_col;
      cout << ( nim ? "Gretel" : "Hansel") << endl;
  }
  return 0;
}