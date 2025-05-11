#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input date
    int month, day;
    cin >> month >> day;
    // Output
    if(month >= 1 && month <= 3)
    {
        // From 21/3 to 31/3 is spring
        if(month == 3 && day >= 21) { cout << "spring"; }
        // From 1/1 to 20/3 is winter
        else { cout << "winter"; }
    }
    if(month >= 4 && month <= 6)
    {
        // From 21/6 to 30/6 is summer
        if(month == 6 && day >= 21) { cout << "summer"; }
        // From 1/4 to 20/6 is spring
        else { cout << "spring"; }
    }
    if(month >= 7 && month <= 9)
    {
        // From 21/9 to 30/9 is fall
        if(month == 9 && day >= 21) { cout << "fall"; }
        // From 1/7 to 20/9 is summer
        else { cout << "summer"; }
    }
    if(month >= 10 && month <= 12)
    {
        // From 21/12 to 31/12 is winter
        if(month == 12 && day >= 21) { cout << "winter"; }
        // From 1/10 to 20/12
        else { cout << "fall"; }
    }
    return 0;
}