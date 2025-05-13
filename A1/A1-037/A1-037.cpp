#include<iostream>
using namespace std;

// Roman number on each digits
string THOUSANDS[4] =  {"", "M", "MM", "MMM"};
string HUNDREDS[10] =  {"", "C", "CC", "CCC", "CD",
                        "D", "DC", "DCC", "DCCC", "CM"};
string TENS[10]     =  {"", "X", "XX", "XXX", "XL",
                        "L", "LX", "LXX", "LXXX", "XC"};
string ONES[10]     =  {"", "I", "II", "III", "IV",
                        "V", "VI", "VII", "VIII", "IX"};

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int num;
    cin >> num;
    // Output
    cout << THOUSANDS[num / 1000];
    num %= 1000;
    cout << HUNDREDS[num / 100];
    num %= 100;
    cout << TENS[num / 10];
    num %= 10;
    cout << ONES[num];
    return 0;
}