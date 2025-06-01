#include<iostream>
using namespace std;

int N, cnt = 0;
string id01, id02;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input id and its length
    cin >> N >> id01 >> id02;
    // Consider the sum of each digits
    for(int i = 0; i < N; i++)
    {
        // Convert char to int by minus with '0'
        int sum = (id01[i] - '0') + (id02[i] - '0');
        // Count amount of digits which the sum is not 9
        if(sum != 9) { cnt++; }
    }
    // Output
    if(cnt > 0) { cout << "NO " << cnt; }
    else { cout << "YES"; }
    return 0;
}