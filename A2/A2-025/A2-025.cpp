#include<iostream>
#include<vector>
using namespace std;

int N, row, col, safePoints, pos[2];
vector<vector<int>> grid;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input dimension of a grid
    cin >> row >> col;
    grid.assign(row, vector<int>(col, 0));
    safePoints = row * col;
    // Input rabbit position
    cin >> pos[0] >> pos[1];

    // Input infected points and mark on grid
    cin >> N;
    while(N--)
    {
        // Input infected points
        int r, c;
        cin >> r >> c;

        // Mark infected points
        for(int dr = -2; dr <= 2; dr++)
        {
            for(int dc = -2; dc <= 2; dc++)
            {
                // Check out of bounds
                if(r + dr < 0 || r + dr >= row || c + dc < 0 || c + dc >= col) 
                {
                    continue;
                }
                // Decrease safe points
                if(grid[r + dr][c + dc] == 0) { safePoints--; }
                
                // Mark 100% infected points
                if(dr == 0 && dc == 0)
                {
                    grid[r + dr][c + dc] = 100;
                }
                // Mark 60% infected points
                else if(abs(dr) <= 1 && abs(dc) <= 1)
                {
                    grid[r + dr][c + dc] = max(grid[r + dr][c + dc], 60);
                }
                // Mark 20% infected points
                else
                {
                    grid[r + dr][c + dc] = max(grid[r + dr][c + dc], 20);
                }
            }
        }
    }

    // Output
    cout << safePoints << '\n';
    cout << grid[pos[0]][pos[1]] << "%\n";
    return 0;
}