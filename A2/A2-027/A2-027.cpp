#include<iostream>
using namespace std;

int N, maxScore = 0, maxCount = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input number of scores
    cin >> N;
    // Find maximum score and count them
    while(N--)
    {
        int score;
        cin >> score;
        if(score == maxScore) { maxCount++; }
        else if(score > maxScore)
        {
            maxScore = score;
            maxCount = 1;
        }
    }
    // Output
    cout << maxScore << '\n' << maxCount;
    return 0;
}