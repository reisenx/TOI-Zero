#include<iostream>
#include<vector>
using namespace std;

int R, C;
const char STATUS[3] = {'-', '*', '*'};
vector<vector<int>> map;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input map dimension
    cin >> R >> C;
    map.assign(R, vector<int>(C, 0));
    // Input map
    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
        {
            char status;
            cin >> status;
            if(status == '*') { map[r][c] = 1; }
        }
    }

    // Flood expands from above
    for(int r = 0; r < R - 1; r++)
    {
        for(int c = 0; c < C; c++)
        {
            if(map[r][c] == 1 && map[r + 1][c] == 0)
            {
                map[r + 1][c] = 2;
            }
        }
    }

    // Output
    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
        {
            cout << STATUS[map[r][c]] << ' ';
        }
        cout << '\n';
    }
    return 0;
}