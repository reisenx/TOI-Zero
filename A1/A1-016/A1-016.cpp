#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    string id;
    cin >> id;
    // Output
    if(id[2] == '1' && id[3] == '6') { cout << "yes"; }
    else {cout << "no"; }
    return 0;
}