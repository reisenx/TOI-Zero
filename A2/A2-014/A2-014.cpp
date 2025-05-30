#include<iostream>
using namespace std;

int talismanSize, size01, size02, wCount = 0, wConsec = 0, wMaxConsec = 0;
string name01, name02, talisman;

/**
 * @brief Check if letter a or b contains 'l', 'o', 'v' or 'e'
 *
 * @param a is a first letter
 * @param b is a second letter
 * @return true if the letter contains 'l', 'o', 'v' or 'e'
 * @return false if the letter contains 'l', 'o', 'v' or 'e'
 */
bool isLove(char &a, char &b)
{
    bool c1 = (a == 'l' || b == 'l' || a == 'L' || b == 'L');
    bool c2 = (a == 'o' || b == 'o' || a == 'O' || b == 'O');
    bool c3 = (a == 'v' || b == 'v' || a == 'V' || b == 'V');
    bool c4 = (a == 'e' || b == 'e' || a == 'E' || b == 'E');
    return c1 || c2 || c3 || c4;
}

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input names
    cin >> name01 >> name02;
    size01 = name01.size();
    size02 = name02.size();

    // Add '$' and 'w' to a talisman
    talismanSize = max(size01, size02);
    for(int i = 0; i < talismanSize; i++)
    {
        // Add 'w' when a letter contains 'l', 'o', 'v' or 'e'
        if(isLove(name01[i % size01], name02[i % size02]))
        {
            talisman += 'w';
            // Count amount of 'w' and consecutive 'w'
            wCount++;
            wConsec++;
        }
        // Otherwise, add '$'
        else
        { 
            talisman += '$';
            // Find maximum consecutive 'w' and reset consecutive counter
            wMaxConsec = max(wMaxConsec, wConsec);
            wConsec = 0;
        }
    }
    // Don't forget to find maximum consecutive 'w' once again
    wMaxConsec = max(wMaxConsec, wConsec);

    // Add maximum consecutive 'w' at the end, if w amount is odd
    if(wCount % 2 == 1)
    {
        talisman += to_string(wMaxConsec);
    }
    // Add '#' if maximum consecutive is less than 2 and w amount is even
    else if(wMaxConsec < 2) { talisman += '#'; }

    // Output
    cout << talisman;
    return 0;
}