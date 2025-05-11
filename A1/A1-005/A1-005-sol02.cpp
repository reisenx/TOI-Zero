#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input day and month
    pair<int, int> date;
    cin >> date.first >> date.second;
    // Output
    if(date < make_pair(3, 21)) { cout << "winter"; }
    else if(date < make_pair(6, 21)) { cout << "spring"; }
    else if(date < make_pair(9, 21)) { cout << "summer"; }
    else if(date < make_pair(12, 21)) { cout << "fall"; }
    else { cout << "winter"; }
    return 0;
}