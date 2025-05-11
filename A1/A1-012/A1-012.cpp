#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int num01;
    char operation;
    cin >> num01 >> operation;
    // Reverse 2-digit number
    int num02 = ((num01 % 10) * 10) + (num01 / 10);
    // Output
    if(operation == '+')
    {
        cout << num01 << " + " << num02 << " = " << num01 + num02;
    }
    else if(operation == '*')
    {
        cout << num01 << " * " << num02 << " = " << num01 * num02;
    }
    return 0;
}