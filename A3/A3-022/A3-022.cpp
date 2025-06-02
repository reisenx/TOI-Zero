#include<iostream>
using namespace std;

bool degree[360];
int N, degCount = 0, maxDegCount = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input light interval and mark as lighted
    cin >> N;
    while(N--)
    {
        int A, B;
        cin >> A >> B;
        if(A > B) { B += 360; }
        
        for(int i = A; i < B; i++)
        {
            if(!degree[i % 360]) { degree[i % 360] = true; }
        }
    }

    // Find maximum lighted interval
    // Case 1: Maximum interval is [A, B] when A < B
    for(int i = 0; i < 360; i++)
    {
        if(degree[i]) { degCount++; }
        else
        { 
            maxDegCount = max(maxDegCount, degCount);
            degCount = 0;
        }
    }
    maxDegCount = max(maxDegCount, degCount);

    // Case 2: Maximum interval is [A, B] when A > B
    if(maxDegCount < 360)
    {
        int A = 359, B = 0;
        while(degree[A]) { A--; }
        while(degree[B]) { B++; }
        degCount = (B + 360) - A - 1;
    }
    maxDegCount = max(maxDegCount, degCount);

    // Output
    cout << maxDegCount << '\n';
    return 0;
}