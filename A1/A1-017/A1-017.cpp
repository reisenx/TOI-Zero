#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int y1, m1, d1, y2, m2, d2;
    cin >> y1 >> m1 >> d1 >> y2 >> m2 >> d2;
    // Output
    // Compare year
    if(y1 < y2) { cout << 1; }
    else if(y2 < y1) { cout << 2; }
    else
    {
        // Compare month
        if(m1 < m2) { cout << 1; }
        else if(m2 < m1) { cout << 2; }
        else
        {
            // Compare day
            if(d1 < d2) { cout << 1; }
            else if(d2 < d1) { cout << 2; }
            else { cout << 0; }
        }
    }
    return 0;
}