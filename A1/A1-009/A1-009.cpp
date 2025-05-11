#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input score
    int midterm, finals;
    cin >> midterm >> finals;
    // Output
    int total = midterm + finals;
    cout << total << '\n';
    
    if(total >= 50) { cout << "pass"; }
    else { cout << "fail"; }
    return 0;
}