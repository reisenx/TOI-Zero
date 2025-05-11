#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    char letter;
    cin >> letter;
    // Output
    if(letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u')
    {
        cout << "yes";
    }
    else { cout << "no"; }
    return 0;
}