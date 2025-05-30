#include<iostream>
using namespace std;

int width, height, level, pricePerMeter, length, price;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input
    cin >> width >> height >> level >> pricePerMeter;
    // Calculate total fence length and price
    length = (2 * (width + height)) * level;
    price = length * pricePerMeter;
    // Output
    cout << length << '\n' << price;
    return 0;
}