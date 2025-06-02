#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N, dist = 0;
vector<int> pillars;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input pillar amount
    cin >> N;
    pillars.resize(N);
    // Input pillar length
    for(int i = 0; i < N; i++) { cin >> pillars[i]; }
    // Sort pillar length in ascending order
    sort(pillars.begin(), pillars.end());
    // Calculate total distance
    int curr = 0;
    for(int i = 0; i < N; i++)
    {
        curr += pillars[i]; // Calculate current total pillar length
        dist += curr * 2;   // Calculate total distance
    }
    // Output
    cout << dist << '\n';
    return 0;
}