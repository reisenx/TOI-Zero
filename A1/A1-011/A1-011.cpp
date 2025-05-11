#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    string text;
    cin >> text;
    // Output
    char letter = text[0];
    int cnt = 1;
    for(int i = 1; i < text.size(); i++)
    {
        // Count if it is the same letter
        if(text[i] == letter) { cnt++; }
        // Otherwise, output and change to the new letter
        else
        {
            cout << cnt << letter;
            letter = text[i];
            cnt = 1;
        }
    }
    // Don't forget to output the last one
    cout << cnt << letter;
    return 0;
}