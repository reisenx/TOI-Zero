#include<iostream>
using namespace std;

int arr[5][5], row[5] = {0, 0, 0, 0, 0}, col[5] = {0, 0, 0, 0, 0};
int r = -1, c = -1;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input 5 x 5 array
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            cin >> arr[i][j];
            // Calculate row and column sum
            row[i] += arr[i][j];
            col[j] += arr[i][j];
        }
    }
    // Find row and column that has odd sum
    for(int i = 0; i < 5; i++)
    {
        if(row[i] % 2 == 1) { r = i; }
        if(col[i] % 2 == 1) { c = i; }
    }
    // Output
    cout << r << ' ' << c;
    return 0;
}