#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    int n;
    cin >> n;
    // Calculate sum
    int ans = 0;
    for(int i = 1; i <= n; i++) { ans += i*i; }
    // Output
    cout << ans;
    return 0;
}