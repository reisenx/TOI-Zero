#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    int n;
    cin >> n;
    // Output
    for(int i = 1; i <= n; i++)
    {
        if(i % 5 == 0) { cout << 'X'; }
        else { cout << '*'; }
    }
    return 0;
}