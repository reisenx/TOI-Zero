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
    for(int i = 0; i < n; i++) { cout << '*'; }
    cout << '\n';
    for(int i = 0; i < n - 2; i++) { cout << '*'; }
    cout << '\n';
    for(int i = 0; i < n - 4; i++) { cout << '*'; }
    return 0;
}