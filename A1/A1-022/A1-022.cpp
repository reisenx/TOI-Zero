#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int day, month;
    cin >> day >> month;
    // Output
    pair<int,int> date = {month, day};
    if(date <= make_pair(1, 19)) { cout << "capricorn"; }
    else if(date <= make_pair(2, 18)) { cout << "aquarius"; }
    else if(date <= make_pair(3, 20)) { cout << "pisces"; }
    else if(date <= make_pair(4, 19)) { cout << "aries"; }
    else if(date <= make_pair(5, 20)) { cout << "taurus"; }
    else if(date <= make_pair(6, 21)) { cout << "gemini"; }
    else if(date <= make_pair(7, 22)) { cout << "cancer"; }
    else if(date <= make_pair(8, 22)) { cout << "leo"; }
    else if(date <= make_pair(9, 22)) { cout << "virgo"; }
    else if(date <= make_pair(10, 23)) { cout << "libra"; }
    else if(date <= make_pair(11, 21)) { cout << "scorpio"; }
    else if(date <= make_pair(12, 21)) { cout << "sagittarius"; }
    else { cout << "capricorn"; }
    return 0;
}