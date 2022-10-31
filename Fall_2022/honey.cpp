#include <iostream>
#include <cstring>

using namespace std;

static const int max_steps = 14;

static const int max_tiles = max_steps * 2 + 1; 
int steps_[max_tiles][max_tiles][max_steps];

int w(const int x, const int y, const int s) {
  if (s == 0) {
    if (x == 0 && y == 0) {
      return 1;
    } else {
      return 0;
    }
  }

  if (steps_[x+max_steps][y+max_steps][s] != -1) {
    return steps_[x+max_steps][y+max_steps][s];
  }

  auto output = int{0};
  output += w(x-1, y-1, s-1);
  output += w(x, y-1, s-1);
  output += w(x+1, y, s-1);
  output += w(x+1, y+1, s-1);
  output += w(x, y+1, s-1);
  output += w(x-1, y, s-1);
  steps_[x+max_steps][y+max_steps][s] = output;

  return output;
}

int Walk(const int number_of_steps)
{
    return w(0, 0, number_of_steps);
}
int main()
{
    memset(steps_, -1, sizeof(steps_));
    int number_of_test_cases = 0;
    cin >> number_of_test_cases;
    
    for (int test_case = 0; test_case < number_of_test_cases; ++test_case) {
        int number_of_steps = 0;
        cin >> number_of_steps;

        cout << Walk(number_of_steps) << "\n";
  }
    
}