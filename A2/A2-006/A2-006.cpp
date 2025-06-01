#include<iostream>
#include<vector>
#include<stack>
using namespace std;

int N, ans = 0;
const int DR[2] = {-1, 0}, DC[2] = {0, -1}; // Up and Right directions
vector<vector<int>> map;

/**
 * @brief Depth First Search (DFS) algorithm on a 2D grid implemented by a stack.
 *        Starts at the bottom-right, and go up and right direction only.
 */
void dfs()
{
    // Start at the bottom-right of a map
    stack<pair<int, int>> grid;
    grid.push(make_pair(N - 1, N - 1));
    map[N - 1][N - 1] = 1;
    ans++;

    // Traverse to adjacent grid
    while(!grid.empty())
    {
        // Get current grid information
        int r = grid.top().first;
        int c = grid.top().second;
        grid.pop();
        
        for(int i = 0; i < 2; i++)
        {
            // Check out of bounds
            if(r + DR[i] < 0 || r + DR[i] >= N || c + DC[i] < 0 || c + DC[i] >= N)
            {
                continue;
            }
            // Check obstacle and already passed
            if(map[r + DR[i]][c + DC[i]] != 0) { continue; }
            // Go to that grid and add to a stack
            map[r + DR[i]][c + DC[i]] = 1;
            grid.push(make_pair(r + DR[i], c + DC[i]));
            // Count possible start point
            ans++;
        }
    }
}

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input map
    cin >> N;
    map.assign(N, vector<int>(N, 0));
    for(int r = 0; r < N; r++)
    {
        string row;
        cin >> row;
        for(int c = 0; c < N; c++)
        {
            if(row[c] == 'X') { map[r][c] = -1; }
        }
    }
    // Call DFS function
    dfs();
    // Output
    cout << ans << '\n';
    return 0;
}