#include<iostream>
using namespace std;

const int PRIZE[2][4] = {{100000, 200, 100, 0},
                         {1000000, 2000, 1000, 20}};
int type, cnt = 0;
char lotteryChar, resultChar;
string lotteryNum, resultNum;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input lottery and its result
    cin >> lotteryChar >> lotteryNum;
    cin >> resultChar >> resultNum;

    // Check letter part
    type = (lotteryChar == resultChar);
    // Check number part
    for(int i = 4; i >= 0; i--)
    {
        if(lotteryNum[i] == resultNum[i]) { cnt++; }
        else { break; }
    }
    
    // Output
    if(cnt == 5) { cout << PRIZE[type][0]; }
    else if(cnt >= 3) { cout << PRIZE[type][1]; }
    else if(cnt == 2) { cout << PRIZE[type][2]; }
    else { cout << PRIZE[type][3]; }
    return 0;
}