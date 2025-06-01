#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

int N;
vector<int> sum;
unordered_set<int> unique;

/**
 * @brief Get the sum from P[a] to P[b]
 * 
 * @param a is the start index
 * @param b is the stop index
 * @return int as the sum from P[a] to P[b]
 */
int getSum(int a, int b)
{
    if(a == 0) { return sum[b]; }
    return sum[b] - sum[a - 1];
}

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input prices and calculate prefix sum
    cin >> N;
    sum.resize(N);
    cin >> sum[0];
    for(int i = 1; i < N; i++)
    {
        cin >> sum[i];
        sum[i] += sum[i - 1];
    }
    // Find all unique sum by using unordered set
    for(int i = 0; i < N; i++)
    {
        for(int j = i; j < N; j++)
        {
            unique.insert(getSum(i, j));
        }
    }
    // Output
    cout << unique.size() << '\n';
    return 0;
}