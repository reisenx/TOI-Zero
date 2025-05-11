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
    if(a == b && b == c) { cout << "all the same"; }
    else if(a != b && b != c && a != c) { cout << "all different"; }
    else { cout << "neither"; }
    return 0;
}