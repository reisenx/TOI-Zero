#include<iostream>
#include<vector>
using namespace std;

bool hasAllHole = true;
int N, W, L;
vector<vector<bool>> woods;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    cin >> N >> W >> L;
    woods.assign(N, vector<bool>(W, false));

    // Input position of the hole
    for(int i = 0; i < N; i++)
    {
        int K;
        cin >> K;
        while(K--)
        {
            int hole;
            cin >> hole;
            hole--;

            // Mark [hole - L, hole + L] as a hole
            for(int dl = -L; dl <= L; dl++)
            {
                // Check out of bounds
                if(hole + dl < 0 || hole + dl >= W) { continue; }
                // Mark as a hole
                woods[i][hole + dl] = true;
            }
        }
    }

    // Check hole on all woods
    for(int x = 0; x < W; x++)
    {
        hasAllHole = true;
        for(int i = 0; i < N; i++)
        {
            if(!woods[i][x])
            {
                hasAllHole = false;
                break;
            }
        }
        if(hasAllHole) { break; }
    }

    // Output
    if(hasAllHole) { cout << "1\n"; }
    else { cout << "0\n"; }
    return 0;
}