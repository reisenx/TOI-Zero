#include<iostream>
#include<vector>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input amount of people
    int N;
    cin >> N;
    // Input graph of items flows
    vector<int> graph(N, -1);
    for(int from = 0; from < N; from++)
    {
        int to;
        cin >> to;
        graph[from] = to - 1;
    }

    // Find maximum node amount on cycle on a graph
    // Every node has 1 in-degree and 1 out-degree
    int maxCycleCount = 0;
    vector<bool> isVisited(N, false);
    for(int start = 0; start < N; start++)
    {
        // Find start node of a cycle
        if(isVisited[start]) { continue; }
        
        // Count node on a cycle
        int curr = start;
        int cycleCount = 0;
        while(!isVisited[curr])
        {
            isVisited[curr] = true;
            curr = graph[curr];
            cycleCount++;
        }
        // Find maximum node amount on a cycle
        maxCycleCount = max(maxCycleCount, cycleCount);
    }

    // Output maximum node amount on cycle on a graph
    cout << maxCycleCount;
    return 0;
}