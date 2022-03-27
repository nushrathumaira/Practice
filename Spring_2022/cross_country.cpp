/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;

int main()
{
    //cout<<"Hello World";
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    ll n, source, dest;
    ll visitedEdges = 1;
    cin >> n >> source >> dest;
    vector<vector<ll>> adjMatrix(n);
    for(int i =0; i < n ; i++)
    {
        adjMatrix[i].resize(n);
        for(int j = 0; j < n; j++)
        {
            cin >> adjMatrix[i][j];
        }
    }
    // this will be used for output array, distance[i] holds shortest distance from src to i
    vector<ll> distance(n); 
    //seenset[i] will be true if i is included in shortest path
    vector<bool> seenSet(n,false);
    //we add the first node or source node
    seenSet[source] = true;
    for(int i = 0; i < n; i++)
    {
        distance[i] = adjMatrix[source][i];
    }
    while(visitedEdges != n)
    {
        ll shortest_dist = INT_MAX;
        ll shortest_index;
        // find shortest unseen node
        for(int i =0; i < n; i++)
        {
            if(!seenSet[i] && distance[i] < shortest_dist)
            {
                shortest_dist = distance[i];
                shortest_index = i;
            }
        }
        //// Update dist value of the adjacent vertices of 
        //the vertex with shortest distance picked before
        for(int i =0; i < n; i++)
        {
            //Update distance[i] only if is not in seenSet, there is an edge from
            // shortest_index to i, and total weight of path from src to  i through shortest_index is
            // smaller than current value of dist[i]
            if( adjMatrix[shortest_index][i] != 0 && distance[i] > distance[shortest_index]+adjMatrix[shortest_index][i])
            {
                distance[i] = distance[shortest_index]+adjMatrix[shortest_index][i];
            }
        }
        seenSet[shortest_index] = true;
        visitedEdges++;

        
    }
    
    cout << distance[dest] << endl;
    return 0;
}
