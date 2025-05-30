#include<iostream>
#include<set>
using namespace std;

set<int> unique;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input and Output non-duplicate numbers
    for(int i = 0; i < 10; i++)
    {
        int num;
        cin >> num;
        bool isUnique = unique.insert(num).second;
        if(isUnique) { cout << num << " "; }
    }
    return 0;
}