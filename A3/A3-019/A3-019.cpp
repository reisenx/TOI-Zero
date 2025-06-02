#include<iostream>
#include<vector>
using namespace std;

int N, L, maxHeight = 0;
vector<int> heights, extra;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input customer amount and extra customer amount
    cin >> N >> L;
    // Input height of each customer
    heights.resize(N);
    for(int i = 0; i < N; i++) { cin >> heights[i]; }
    // Input index of extra customer
    extra.resize(L);
    for(int i = 0; i < L; i++)
    { 
        cin >> extra[i]; 
        extra[i]--; 
    }
    // Output
    int idx = 0;
    for(int i = 0; i < N; i++)
    {
        // Skip, if no more extra customer
        if(idx >= L) { continue; }
        // Current customer is the tallest
        if(heights[i] > maxHeight)
        {
            maxHeight = heights[i];
            // The extra customer is the tallest
            if(i == extra[idx])
            {
                cout << "0\n";
                idx++;
            }
        }
        // The extra customer is not the tallest
        else if(i == extra[idx])
        {
            cout << (maxHeight + 1) - heights[i] << '\n';
            idx++;
        }
    }
    return 0;
}