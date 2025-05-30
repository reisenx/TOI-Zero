#include<iostream>
using namespace std;

char bobaType, teaType;
int total = 0, bobaAmount, teaSweet, teaAmount;
int BOBA_CALORIES[3] = {5, 3, 2};
int TEA_CALORIES[3][3] = {{12, 18, 25}, {15, 20, 30}, {10, 15, 20}};

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input boba details
    cin >> bobaType >> bobaAmount;
    if(bobaType == 'H') { total += BOBA_CALORIES[0] * bobaAmount; }
    if(bobaType == 'O') { total += BOBA_CALORIES[1] * bobaAmount; }
    if(bobaType == 'J') { total += BOBA_CALORIES[2] * bobaAmount; }
    // Input tea details
    cin >> teaType >> teaSweet >> teaAmount;
    if(teaType == 'R') { total += TEA_CALORIES[0][teaSweet - 1] * teaAmount; }
    if(teaType == 'T') { total += TEA_CALORIES[1][teaSweet - 1] * teaAmount; }
    if(teaType == 'M') { total += TEA_CALORIES[2][teaSweet - 1] * teaAmount; }
    // Output
    cout << total;
}