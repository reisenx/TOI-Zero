#include<iostream>
using namespace std;

int firstB = -1, consecU = 0, maxConsecU = 0;
bool isCountStart = false;
string txt, newText;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input string
    cin >> txt;
    for(int i = 0; i < txt.size(); i++)
    {
        // Start counting
        if(txt[i] == 'B' || txt[i] == 'b')
        {
            // Reset counter
            isCountStart = true;
            maxConsecU = max(maxConsecU, consecU);
            consecU = 0;
            // Get index of the first appearance of 'B'
            if(firstB == -1) { firstB = i; }
        }
        else if(isCountStart && (txt[i] == 'U' || txt[i] == 'u')) 
        { 
            consecU++;
        }
        // Stop counting
        else
        {
            // Reset counter
            isCountStart = false;
            maxConsecU = max(maxConsecU, consecU);
            consecU = 0;
        }
    }
    // Find maximum consecutive 'U' once again
    maxConsecU = max(maxConsecU, consecU);
    
    // Output (Has 'BUU')
    if(maxConsecU > 1)
    {
        cout << "Yes " << maxConsecU << '\n';
    }
    // Output (Has no 'BUU', but has 'B')
    else if(firstB != -1)
    {
        // Output same letter until the first appearance of 'B'
        for(int i = 0; i <= firstB; i++)
        {
            cout << txt[i];
        }
        // Spams 'U' until the end of a text
        for(int i = firstB + 1; i < txt.size(); i++)
        {
            cout << 'U';
        }
    }
    // Output (Has no 'BUU' nor 'B')
    else
    {
        // Output 'BUU' in loop
        for(int i = 0; i < txt.size(); i++)
        {
            if(i % 3 == 0) { cout << 'B'; }
            else { cout << 'U'; }
        }
    }
    return 0;
}