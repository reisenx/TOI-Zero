#include<iostream>
#include<vector>
using namespace std;

int N, K, T, curr = 1, ans = 1;
vector<bool> received;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    cin >> N >> K >> T;

    // Pass the box to next K person (starts at person number 1)
    // Note that person number N is in index 0
    received.assign(N, false);
    received[1] = true;
    curr = (curr + K) % N;
    while(ans < N)
    {
        // Current person has not received the box yet
        if(!received[curr])
        {
            received[curr] = true;
            ans++;
        }
        // The box come back to person number 1
        if(curr == 1) { break; }
        // The box is in the thief hands
        if(curr == (T % N)) { break; }
        // Pass to the next person
        curr = (curr + K) % N;
    }

    // Output
    cout << ans;
    return 0;
}