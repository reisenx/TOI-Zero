#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int a, b, c;
    cin >> a >> b >> c;
    // Output
    if(a < b && b < c) { cout << "increasing"; }
    else if(a > b && b > c) { cout << "decreasing"; }
    else { cout << "neither"; }
    return 0;
}