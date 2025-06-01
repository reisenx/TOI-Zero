#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N, fatCount = 0;
vector<pair<int, string>> rabbits;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input number of rabbits
    cin >> N;
    // Input rabbit information
    for(int i = 0; i < N; i++)
    {
        string name;
        int weight;
        cin >> name >> weight;
        rabbits.push_back(make_pair(weight, name));
        // Count fat rabbits
        if(weight > 15) { fatCount++; }
    }
    // Sort rabbit by weights
    sort(rabbits.begin(), rabbits.end());
    // Output
    cout << fatCount << '\n';
    cout << rabbits[N - 1].second << ' ' << rabbits[N - 1].first << '\n';
    return 0;
}