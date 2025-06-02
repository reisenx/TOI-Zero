#include<iostream>
using namespace std;

int N, S, minDist, maxDist;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input mountain amount and road length
    cin >> N >> S;

    // Calculate distance on a road
    minDist = S;
    maxDist = S;
    while(N--)
    {
        // Input mountain height
        int H;
        cin >> H;
        // Can be either type 1 or 2 mountain
        if(H % 12 == 0)
        {
            minDist -= (H / 3) * 10;
            maxDist -= (H / 4) * 10;
        }
        // Type 1 mountain
        else if(H % 3 == 0)
        {
            minDist -= (H / 3) * 10;
            maxDist -= (H / 3) * 10;
        }
        // Type 2 mountain
        else if(H % 4 == 0)
        {
            minDist -= (H / 4) * 10;
            maxDist -= (H / 4) * 10;
        }
    }

    // Output
    cout << minDist << ' ' << maxDist << '\n';
    return 0;
}