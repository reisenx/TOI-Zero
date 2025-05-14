#include<iostream>
#include<vector>
using namespace std;

int n, ans = 0;
vector<int> trees;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input trees height
    cin >> n;
    trees.resize(n);
    for(int i = 0; i < n; i++) { cin >> trees[i]; }
    // Count amount of trees that has no taller adjacent trees
    if(trees[0] >= trees[1]) { ans++; }
    for(int i = 1; i < n - 1; i++)
    {
        if(trees[i] >= trees[i - 1] && trees[i] >= trees[i + 1])
        {
            ans++;
        }
    }
    if(trees[n - 1] >= trees[n - 2]) { ans++; }
    // Output
    cout << ans;
    return 0;
}