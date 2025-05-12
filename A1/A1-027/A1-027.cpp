#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    string text;
    cin >> text;
    // Output
    for(int i = text.size() - 1; i >= 0; i--)
    {
        text[i] = tolower(text[i]);
        cout << text[i];
    }
    return 0;
}