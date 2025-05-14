#include<iostream>
#include<vector>
using namespace std;

int N, C;
vector<vector<int>> results;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input result matrix
    cin >> N >> C;
    results.assign(N, vector<int>(N));
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
        {
            cin >> results[i][j];
        }
    }

    // Tournament
    vector<int> thisRound;
    for(int i = 1; i <= N; i++) { thisRound.push_back(i); }
    
    for(int round = N; round > 0; round /= 2)
    {
        vector<int> nextRound;
        for(int i = 0; i < thisRound.size() / 2; i++)
        {
            // Find a winner
            int teamA = thisRound[2 * i];
            int teamB = thisRound[(2 * i) + 1];
            int winner = results[teamA - 1][teamB - 1];

            // Team has the special card
            if(teamA == C && teamA != winner) { winner = teamA; C = 0; }
            if(teamB == C && teamB != winner) { winner = teamB; C = 0; }
            nextRound.push_back(winner);
        }
        // Output
        if(nextRound.size() == 1)
        {
            cout << nextRound[0];
            break;
        }
        // Copy vector
        thisRound = nextRound;
    }
    return 0;
}