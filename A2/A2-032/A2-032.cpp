#include<iostream>
#include<vector>
using namespace std;

int R, C, P, ans = 0;
vector<vector<int>> grid, dp;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input dimension of a grid
    cin >> R >> C;
    grid.assign(R, vector<int>(C, 0));
    dp.assign(R, vector<int>(C, 0));

    // Input position of pokemon
    cin >> P;
    while(P--)
    {
        int r, c;
        cin >> r >> c;
        // Update amount of pokemon on grid
        grid[r][c]++;
        // Mark position (r, c) as unavailable to catch
        dp[r][c] = -1;
        // Update catch pokemon amount on adjacent grid
        for(int dr = -1; dr <= 1; dr++)
        {
            for(int dc = -1; dc <= 1; dc++)
            {
                // Check out of bounds
                if(r + dr < 0 || r + dr >= R || c + dc < 0 || c + dc >= C)
                {
                    continue;
                }
                // Skip unavailable position
                if(dp[r + dr][c + dc] == -1) { continue; }
                // Skip current grid
                if(dr == 0 && dc == 0) { continue; }
                // Add catch pokemon amount
                dp[r + dr][c + dc]++;
            }
        }
    }

    // Find maximum catch pokemon amount
    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
        {
            ans = max(ans, dp[r][c]);
        }
    }
    cout << ans << '\n';
    return 0;
}