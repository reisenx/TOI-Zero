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
    if(a <= b && a <= c) { cout << a; }
    else if(b <= a && b <= c) { cout << b; }
    else if(c <= a && c <= b) { cout << c; }
    return 0;
}