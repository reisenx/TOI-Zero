#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int num;
    cin >> num;
    // Output
    for(int i = num - (num % 10); i >= 0; i -= 10)
    {
        cout << i << ' ';
    }
    return 0;
}