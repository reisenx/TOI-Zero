#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int n;
    cin >> n;
    // Find minimum
    int num, minimum;
    cin >> num;
    minimum = num;
    for(int i = 1; i < n; i++)
    {
        cin >> num;
        minimum = min(minimum, num);
    }
    // Output
    cout << minimum;
    return 0;
}