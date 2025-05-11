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
    if(id.size() == 13) { cout << "yes"; }
    else { cout << "no"; }
    return 0;
}