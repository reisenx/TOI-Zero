#include<iostream>
using namespace std;

int N;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input triangle height
    cin >> N;
    // Output
    for(int i = 1; i <= N; i++)
    {
        // Top part of the triangle
        if(i == 1) { cout << 0; }
        // Base of the triangle
        else if(i == N)
        {
            for(int j = 0; j < N; j++) { cout << 0 << ' '; }
        }
        // Middle part of the triangle
        else
        {
            // Left border
            cout << 0 << ' ';
            // Inside triangle
            for(int j = 0; j < i - 2; j++) { cout << 1 << ' '; }
            // Right border
            cout << 0;
        }
        // Go to next line
        cout << '\n';
    }
    return 0;
}