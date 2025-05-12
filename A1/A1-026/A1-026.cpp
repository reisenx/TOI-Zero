#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int a, b, c;
    cin >> a >> b >> c;
    // Count odd numbers
    int odd = (a % 2) + (b % 2) + (c % 2);
    // Output
    cout << "even " << 3 - odd << '\n';
    cout << "odd " << odd << '\n';
    return 0;
}