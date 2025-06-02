#include<iostream>
#define K 2
#define LENGTH 300
using namespace std;

int L, N, ans = 0;
int road[(K * LENGTH) + 1];


int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input length of a road and bridge amount
    cin >> L >> N;
    // Input bridge
    while(N--)
    {
        // Input bridge interval
        int start, stop;
        cin >> start >> stop;
        // Update road array (1 block = 1/K meters)
        for(int i = (K * start) + 1; i < (K * stop); i++)
        {
            road[i]++;
            ans = max(ans, road[i]); // Find maximum bridge
        }
    }
    // Output
    cout << ans << '\n';
    return 0;
}