#include<iostream>
#include<vector>
using namespace std;

int R, C;
const char SYMBOL[4] = {'-', '+', 'x', '*'};
vector<vector<vector<int>>> img;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input images dimension
    cin >> R >> C;
    img.assign(2, vector<vector<int>>(R, vector<int>(C)));
    // Input images
    for(int i = 0; i < 2; i++)
    {
        for(int r = 0; r < R; r++)
        {
            string symbol;
            cin >> symbol;
            for(int c = 0; c < C; c++)
            {
                if(symbol[c] == '-') { img[i][r][c] = 0; }
                if(symbol[c] == '+') { img[i][r][c] = 1; }
                if(symbol[c] == 'x') { img[i][r][c] = 2; }
            }
        }
    }

    // Output overlapped images
    for(int r = 0; r < R; r++)
    {
        for(int c = 0; c < C; c++)
        {
            int s1 = img[0][r][c];
            int s2 = img[1][r][c];
            // Both image has same symbol
            if(s1 == s2) { cout << SYMBOL[s1]; }
            // Both image has different symbol
            else { cout << SYMBOL[s1 + s2]; }
        }
        cout << '\n';
    }
    return 0;
}