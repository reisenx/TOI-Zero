#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    string letter, num;
    cin >> letter >> num;
    // Output
    if(letter == "H" && num == "4567") { cout << "safe unlocked"; }
    else if(letter == "H") { cout << "safe locked - change digit"; }
    else if(num == "4567") { cout << "safe locked - change char"; }
    else { cout << "safe locked"; }
    return 0;
}