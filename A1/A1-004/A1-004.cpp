#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input score
    int exercise, midterm, finals;
    cin >> exercise >> midterm >> finals;
    // Output
    if(exercise >= 5 && midterm >= 20 && finals >= 25)
    {
        cout << "pass";
    }
    else { cout << "fail"; }
    return 0;
}