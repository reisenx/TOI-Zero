#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    int year;
    cin >> year;
    // Output
    if(year < 1582) { cout << "yes"; }
    else if(year % 400 == 0) { cout << "yes"; }
    else if(year % 4 == 0 && year % 100 != 0) { cout << "yes"; }
    else { cout << "no"; }
    return 0;
}