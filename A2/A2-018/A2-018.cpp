#include<iostream>
using namespace std;

char initial;
int length, idx;
string COLORS[3] = {"Red", "Green", "Blue"};

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input initial color and length
    cin >> initial >> length;
    if(initial == 'R') { idx = 0; }
    if(initial == 'G') { idx = 1; }
    if(initial == 'B') { idx = 2; }
    // Output
    for(int step = 0; step < length; step++)
    {
        cout << COLORS[idx] << ' ';
        idx = (idx + 1) % 3;
    }
    return 0;
}