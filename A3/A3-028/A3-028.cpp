#include<iostream>
#include<vector>
using namespace std;

int R, C, B;
vector<vector<int>> bombCount;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input map dimension
    cin >> R >> C;
    bombCount.assign(R, vector<int>(C, 0));
    // Input bomb position
    cin >> B;
    while(B--)
    {
        int r, c;
        cin >> r >> c;
        // Mark bomb position as unavailable
        bombCount[r][c] = -1;
        // Add 1 to bomb counter in all adjacent grid
        for(int dr = -1; dr <= 1; dr++)
        {
            for(int dc = -1; dc <= 1; dc++)
            {
                // Check out of bounds
                if(r + dr < 0 || r + dr >= R || c + dc < 0 || c + dc >= C)
                {
                    continue;
                }
                // Skip bomb position
                if(bombCount[r + dr][c + dc] == -1) { continue; }
                bombCount[r + dr][c + dc]++;
            }
        }
    }

    // Output
    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
        {
            if(bombCount[r][c] == -1) { cout << "x "; }
            else { cout << bombCount[r][c] << ' '; }
        }
        cout << '\n';
    }
    return 0;
}