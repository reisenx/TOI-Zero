#include<iostream>
using namespace std;

int consecA = 0, maxConsecA = 0;
bool isUnknown = true, isRabbit = true;
string txt;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input string and make it all lowercase
    cin >> txt;
    for(int i = 0; i < txt.size(); i++)
    {
        txt[i] = tolower(txt[i]);
    }

    // Consider string
    for(int i = 0; i < txt.size(); i++)
    {
        bool c1, c2, c3;
        
        // A character that isn't 'i' and 't' detected
        c1 = txt[i] != 'i';
        c2 = txt[i] != 't';
        if(isUnknown && c1 && c2) { isUnknown = false; }
        
        // After 'r' must be 'a'
        if(txt[i] == 'r')
        {
            c1 = (i + 1 == txt.size()); // 'r' is the last character
            c2 = (txt[i + 1] != 'a');   // After 'r' is not 'a'
            
            if(c1 || c2)
            {
                if(c1) { cout << "no " << i; }
                else { cout << "no " << i + 1; }
                
                isRabbit = false;
                break;
            }
        }

        // Before 'a' must be 'r' or 'a'
        if(txt[i] == 'a')
        {
            consecA++;  // Count consecutive 'a'

            c1 = (i == 0);             // 'a' is the first character
            c2 = (txt[i - 1] != 'r');  // Before 'a' is not 'r'
            c3 = (txt[i - 1] != 'a');  // Before 'a' is not 'a'

            if(c1 || (c2 && c3))
            {
                cout << "no " << i << '\n';
                isRabbit = false;
                break;
            }
        }
        // Reset consecutive 'a' counter
        else
        {
            maxConsecA = max(maxConsecA, consecA);
            consecA = 0;
        }

        // After 'b' must be 'i' or 't'
        if(txt[i] == 'b')
        {
            c1 = (i + 1 == txt.size()); // 'b' is the last character
            c2 = (txt[i + 1] != 'i');   // After 'b' is not 'i'
            c3 = (txt[i + 1] != 't');   // After 'b' is not 't'

            if(c1 || (c2 && c3))
            {
                if(c1) { cout << "no " << i; }
                else { cout << "no " << i + 1; }

                isRabbit = false;
                break;
            }
        }
    }
    // Don't forget to find maximum consecutive once again
    maxConsecA = max(maxConsecA, consecA);

    // Output
    if(isUnknown) { cout << "unknown " << txt.size(); }
    else if(isRabbit) { cout << "yes " << maxConsecA; }
    return 0;
}