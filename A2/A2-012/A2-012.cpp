#include<iostream>
using namespace std;

int PRICE[3] = {10, 25, 3}, amount[3];

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input amount of items, and calculate total price
    int totalPrice = 0;
    for(int i = 0; i < 3; i++)
    {
        cin >> amount[i];
        totalPrice += PRICE[i] * amount[i];
    }
    // Output
    cout << totalPrice;
    return 0;
}