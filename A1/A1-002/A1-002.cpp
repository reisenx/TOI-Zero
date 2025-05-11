#include<iostream>
using namespace std;

int money;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input amount of money
    cin >> money;
    // Output amount of coins;
    cout << "10 = " << money / 10 << '\n';
    money %= 10;
    cout << "5 = " << money / 5 << '\n';
    money %= 5;
    cout << "2 = " << money / 2 << '\n';
    money %= 2;
    cout << "1 = " << money << '\n';
    return 0;
}