#include<iostream>
using namespace std;

const int PRICE[2][3] = {{60, 80, 100}, {80, 100, 120}};
const int TOPPING[2] = {15, 10};
char ramenType, ramenSize, toppingType;
int type01, type02, toppingAmount, price = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input ramen information
    cin >> ramenSize >> ramenType;
    if(ramenType == 'R') { type01 = 0; }
    if(ramenType == 'T') { type01 = 1; }
    if(ramenSize == 'S') { type02 = 0; }
    if(ramenSize == 'M') { type02 = 1; }
    if(ramenSize == 'L') { type02 = 2; }
    price += PRICE[type01][type02];

    // Input topping information
    cin >> toppingType;
    if(toppingType == 'P')
    {
        cin >> toppingAmount;
        price += TOPPING[0] * toppingAmount;
    }
    if(toppingType == 'E')
    {
        cin >> toppingAmount;
        price += TOPPING[1] * toppingAmount;
    }

    // Output
    cout << price;
    return 0;
}