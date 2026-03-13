#include<iostream>

int a, b, c;
double total_price = 0;

int main() {
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(0);

    std::cin >> a >> b >> c;
    total_price = (a * 25) + (b * 40) + (c * 55);

    if(a + b + c >= 3) {
        total_price *= 0.9;
    }

    std::cout << (int) total_price << "\n";
    return 0;
}
