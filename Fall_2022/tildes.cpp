#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<int> parent;
vector<int> treeSize;

int findSet(int i)
{
    return (parent[i] == i) ? i : (parent[i]=findSet(parent[i]));
}
/*
int findSet(int e) {
	while (parent[e] != e) {
		parent[e] = parent[parent[e]];
		e = parent[e];
	}
	
	return e;
}
*/
void unionSet(int i, int j)
{
    int root1 = findSet(i);
    int root2 = findSet(j);
    if(root1 != root2)
    {
        if(treeSize[root1] < treeSize[root2])
        {
            int tmp = root1;
            root1 = root2;
            root2 = tmp;
        }
        parent[root2] = root1;
        treeSize[root1] += treeSize[root2];
    }
}
int main()
{
    int n,q, a, b;
    char x;
    cin >> n >> q;
    
    for(int i = 0; i < n; i++)
    {
        parent.push_back(i);
        treeSize.push_back(1);
    }
    for(int i =0; i < q; i++)
    {
        cin >> x;
        if(x=='t')
        {
            cin >> a >> b;
            unionSet(a-1,b-1);
        }
        else
        {
            cin >> a;
            int root = findSet(a-1);
            cout << treeSize[root] << "\n";
        }
    }
    
    return 0;
}