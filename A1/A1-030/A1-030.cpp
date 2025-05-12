#include<iostream>
using namespace std;

int n, ans = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input amount of pairs
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        // Input number of each pair
        int a, b;
        cin >> a >> b;
        // Calculate sum
        ans += max(a, b);

        // Output maximum number of a pair
        cout << max(a, b);
        // Output operator
        if(i < n) { cout << " + "; }
    }
    // Output sum
    if(n > 1) { cout << " = " << ans; }
    return 0;
}