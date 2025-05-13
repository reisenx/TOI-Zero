#include<iostream>
using namespace std;

// Fruits calories
int CALORIES[4] = {100, 120, 200, 60};

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input orders until exits
    int order, total_calories = 0;
    cin >> order;
    while(order != 5)
    {
        total_calories += CALORIES[order - 1];
        cin >> order;
    }
    // Output
    cout << "Bye Bye" << '\n';
    cout << "Total Calories: " << total_calories;
    return 0;
}