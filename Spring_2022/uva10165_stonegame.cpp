/***
Jack and Jim are playing an interesting stone game. At the beginning of the game there are N pile(s)
of stones. Each pile has Pi (i = 1..N, 1 = Pi = 2 * 109
) stones. They take turns to take away some
of the stones. There are some rules: they must choose one pile at a time. They can take away any
number of stones except 0, of course, not bigger than the number of stones in the pile. One who takes
away the last stone will win the game. Jack is the first to fetch the match, and Jim is the second. Now
Jack asks you for help, to decide while facing some initializations whether he is sure to win or not.
Input
The input file contains several scenarios. Each of them consists of 2 lines:
The first line consists of a number N. The second line consists of N numbers, meaning Pi (i = 1..N).
There is only one space between two border numbers.
The input file is ended with N = 0.
Output
For each scenario, print a line containing ‘Yes’ if he is sure to win, or ‘No’ otherwise
Sample Input
1
100
3
1 5 1
4
1 1 1 1
0
Sample Output
Yes
Yes
No
***/

#include <iostream>

using namespace std;

int main(void)
{
    int N,sum,t;
    while(cin >> N && N != 0)
    {
       sum = 0;
       while(N--)
       {
          cin >> t;
          sum ^= t; 
       }
       cout << ((sum != 0) ? "Yes" : "No") << endl;
    }
    return 0;
}