#include<iostream>
#include<map>
using namespace std;

map<char, string> NUMS = {{'A', "ace"}, {'J', "jack"}, {'Q', "queen"}, {'K', "king"}};
map<char, string> GROUPS = {{'D', "diamonds"}, {'H', "hearts"}, {'S', "spades"}, {'C', "clubs"}};

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    string card;
    cin >> card;
    // Make name all uppercase
    for(int i = 0; i < card.size(); i++)
    {
        card[i] = toupper(card[i]);
    }
    
    // Output card number
    if(card.size() == 2)
    {
        // Card number are [A, J, Q, K]
        char num = card[0];
        if(NUMS.find(num) != NUMS.end()) { cout << NUMS[num]; }
        // Card number are 2-9
        else { cout << num; }
    }
    // Card number are 10
    else if(card.size() == 3) { cout << 10; }
    
    // Output card group
    char group = card[card.size() - 1];
    cout << " of " << GROUPS[group];
    return 0;
}