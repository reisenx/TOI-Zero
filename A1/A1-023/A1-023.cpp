#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input
    int temp;
    char unit;
    cin >> temp >> unit;
    // Output
    if(unit == 'C' || unit == 'c')
    {
        if(temp <= 0) { cout << "solid"; }
        else if(temp < 100) { cout << "liquid"; }
        else { cout << "gas"; }
    }
    else if(unit == 'F' || unit == 'f')
    {
        if(temp <= 32) { cout << "solid"; }
        else if(temp < 212) { cout << "liquid"; }
        else { cout << "gas"; }
    }
    return 0;
}