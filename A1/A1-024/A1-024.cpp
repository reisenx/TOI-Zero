#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    int year, motor;
    cin >> year >> motor;
    // Output
    int TAX[3][3] = {{1250, 1400, 2000}, 
                     {1100, 1300, 1700},
                     {1000, 1200, 1500}};
    int YEAR_TYPE = 1;
    if(year <= 1990) { YEAR_TYPE = 0; }
    if(year >= 2000) { YEAR_TYPE = 2; }
    
    int MOTOR_TYPE = 1;
    if(motor <= 1500) { MOTOR_TYPE = 0; }
    if(motor > 2000) { MOTOR_TYPE = 2; }

    cout << TAX[YEAR_TYPE][MOTOR_TYPE];
    return 0;
}