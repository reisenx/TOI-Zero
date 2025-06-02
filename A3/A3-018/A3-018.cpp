#include<iostream>
using namespace std;

int L, N, oranges[101];

/**
 * @brief Calculate oranges amount on each layer
 */
void calculateOranges()
{
    oranges[0] = 0;
    for(int i = 1; i <= 100; i++)
    {
        oranges[i] = oranges[i - 1] + (i * i);
    }
}

/**
 * @brief Get the layer number by orage amount using binary search
 *
 * @param N is the orange amount
 * @return int as the layer number
 */
int getOrangeLayer(int &N)
{
    int low = 0, high = 100, layer = -1;
    while(low <= high)
    {
        int mid = (low + high) / 2;
        if(oranges[mid] == N)
        { 
            layer = mid;
            break;
        }
        else if(oranges[mid] < N)
        {
            layer = mid;
            low = mid + 1;
        }
        else { high = mid - 1; }
    }
    return layer;
}

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input layer and orange amount
    cin >> L >> N;

    // Output
    // 1. Find layer number of oranges that taken off
    // 2. Calculate [total layers - taken off layers]
    calculateOranges();
    cout << L - getOrangeLayer(N);
    return 0;
}