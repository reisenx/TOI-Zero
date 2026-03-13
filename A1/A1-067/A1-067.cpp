#include <bits/stdc++.h>
using namespace std;

string is_member;
int item_count;
double total_price = 0.0;

int main () {
    cin >> is_member;
    
    cin >> item_count;
    for (int i = 0; i < item_count; i++) {
        double price;
        cin >> price;
        total_price += price;
    }

    if (is_member == "Y") {
        total_price *= 0.95;
    }

    if (is_member == "N" && total_price >= 500) {
        total_price *= 0.97;
    }

    cout << fixed << setprecision(2);
    cout << round(total_price * 100.0) / 100.0 << endl;
}