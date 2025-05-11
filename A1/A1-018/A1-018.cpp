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
    string roman[9] = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    if(num > 0 && num <= 9) { cout << roman[num - 1]; }
    else if(num < 0) { cout << "Error : Please input positive number"; }
    else { cout << "Error : Out of range"; }
    return 0;
}