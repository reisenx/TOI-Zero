#include<iostream>
#include<vector>
using namespace std;

int N, S, ans = 0;
vector<int> toWho;
vector<bool> received;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input student amount and start point
    cin >> N >> S;
    // Input message forward graph
    toWho.assign(N, 0);
    for(int i = 0; i < N; i++)
    {
        cin >> toWho[i];
        toWho[i]--;
    }

    // Count student amount who get a message
    received.assign(N, false);
    int curr = S - 1;
    while(true)
    {
        // The previous student didn't forward a message
        if(curr == -1) { break; }
        // The current student already got a message
        if(received[curr]) { break; }
        // The current student received a message
        received[curr] = true;
        ans++;  // Counting...
        // Go to the next student
        curr = toWho[curr];
    }

    // Output
    cout << ans << '\n';
    return 0;
}