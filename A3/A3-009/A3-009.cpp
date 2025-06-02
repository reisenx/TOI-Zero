#include<iostream>
using namespace std;

int N, K, queue[300], hasCustomer = 0, totalCustomer = 0;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    // Input amount of customer and pods
    cin >> N >> K;
    // Input queue line of each customer
    while(N--)
    {
        // Input queue line
        int line;
        cin >> line;
        // Update total customer
        totalCustomer++;
        // Update queue line amount that has customer
        if(queue[line - 1] == 0) { hasCustomer++; }
        // Assign a customer to a queue
        queue[line - 1]++;

        // Check if the customers are ready to get into a pod
        if(hasCustomer == K)
        {
            // Update all queue lines
            for(int i = 0; i < K; i++)
            {
                queue[i]--;         // Remove a customer from a queue
                totalCustomer--;    // Update total customer
                // Update queue line amount that has customer
                if(queue[i] == 0) { hasCustomer--; }
            }
        }
    }

    // Output
    cout << totalCustomer << '\n';
    return 0;
}