#include <bits/stdc++.h>

int main()
{
std::stack<char> _st;
char c;
while(scanf("%c",&c)!=EOF && c != '\n')
{
    if(c=='<') _st.pop();
    else _st.push(c);
}
if(_st.size() > 0)
{
  char buffer[_st.size()+1];
  buffer[_st.size()] = '\0';
  while(!_st.empty())
  {
      buffer[_st.size()-1] = _st.top();
      _st.pop();
  }
  printf("%s",buffer);
}
return 0;
}

