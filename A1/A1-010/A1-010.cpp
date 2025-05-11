#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int age;
    char type;
    cin >> age >> type;
    // Output
    if(age < 18 || type == 's' || type == 'S')
    {
        cout << 20;
    }
    else { cout << 50; }
    return 0;
}