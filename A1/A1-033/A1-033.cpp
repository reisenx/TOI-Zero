#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Vowels
    char VOWELS[5] = {'A', 'E', 'I', 'O', 'U'};
    // Input
    int n, cnt = 0;;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        char letter;
        cin >> letter;
        // Count Vowels
        for(int j = 0; j < 5; j++)
        {
            if(letter == VOWELS[j]) { cnt++; }
        }
    }
    // Output
    cout << cnt;
    return 0;
}