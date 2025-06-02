#include<iostream>
using namespace std;

int L, N, total = 0, n = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input flower layer and flower amount
    cin >> L >> N;
    // Calculate total flower on each layer
    while(total < N)
    {
        // Add flower on the first n * L columns
        total += (n * L) * L;
        // Add flower on the last L column
        total += (L * (L + 1)) / 2;
        // Go to the next layer
        n++;
    }
    // Output
    cout << n << '\n';
    return 0;
}