#include<iostream>
using namespace std;

string name01, name02;

int main()
{
    // This makes std::cin and std::cout faster
    ios::sync_with_stdio(false); cin.tie(0);

    // Input names
    cin >> name01 >> name02;
    // Output
    cout << "Hello " << name01 << " " << name02 << '\n';
    cout << name01[0] << name01[1] << name02[0] << name02[1];
    return 0;
}