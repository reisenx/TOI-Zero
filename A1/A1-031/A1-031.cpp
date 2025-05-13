#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input number
    int num;
    cin >> num;
    // Output
    cout << num / 1000 << ',' << num % 1000;
    return 0;
}