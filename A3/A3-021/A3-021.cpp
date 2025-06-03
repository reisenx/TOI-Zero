#include<iostream>
#include<limits.h>
#include<vector>
using namespace std;

int N, K, fastest = INT_MAX, eliminated = 0;
vector<int> runs;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    cin >> N >> K;
    runs.resize(N);
    // Input time per round of each athlete
    for(int i = 0; i < N; i++) 
    { 
        cin >> runs[i];
        fastest = min(fastest, runs[i]);
    }

    // Calculate time delay of each athlete compared to the fastest
    // Eliminate athlete by consider time delay when running K - 1 rounds
    for(int i = 0; i < N; i++)
    {
        long long delay = 1LL * (runs[i] - fastest) * (K - 1);
        if(delay >= fastest) { eliminated++; }
    }

    // Output
    cout << N - eliminated << '\n';
    return 0;