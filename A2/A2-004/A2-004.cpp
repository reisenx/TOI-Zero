#include<iostream>
#define MAX_SIZE 305
using namespace std;

int n, maxFreq = 0, freq[MAX_SIZE];

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input dishes and find frequency of each dish size
    cin >> n;
    while(n--)
    {
        int dish;
        cin >> dish;
        freq[dish]++;
        maxFreq = max(maxFreq, freq[dish]);
    }
    // Output
    cout << maxFreq;
    return 0;
}