#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    string num;
    cin >> num;
    // Output
    for(int i = num.size() - 1; i >= 0; i--)
    {
        cout << num[i];
    }
    return 0;
}