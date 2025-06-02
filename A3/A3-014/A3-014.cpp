#include<iostream>
using namespace std;

int N, normal = 0, hard = 0, ans = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input task amount
    cin >> N;
    // Count normal work (<= 18 hours) and hard work (> 18 hours)
    while(N--)
    {
        int H;
        cin >> H;
        if(H <= 18) { normal++; }
        else { hard++; }
    }

    // Do hard work, then normal work repeatedly
    int tasks = min(normal, hard);
    ans = tasks * 2;
    // If normal work still remains
    normal -= tasks;
    ans += normal;
    // If hard work still remains
    hard -= tasks;
    ans += max(0, (2 * hard) - 1);
    // Output
    cout << ans;
    return 0;
}