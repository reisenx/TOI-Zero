#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input
    string text;
    cin >> text;
    // Count vowel letters
    int cnt = 0;
    for(int i = 0; i < text.size(); i++)
    {
        if(text[i] == 'a' || text[i] == 'e' || text[i] == 'i' || text[i] == 'o' || text[i] == 'u')
        {
            cnt++;
        }
    }
    // Output
    cout << cnt;
    return 0;
}