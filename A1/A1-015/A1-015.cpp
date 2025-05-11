#include<iostream>
using namespace std;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input
    string first_name, last_name, age;
    cin >> first_name >> last_name >> age;
    // Construct password
    string password = "";
    if(first_name.size() > 5 && last_name.size() > 5)
    {
        password += first_name[0];
        password += first_name[1];
        password += last_name.back();
        password += age.back();
    }
    else
    {
        password += first_name[0];
        password += age;
        password += last_name.back();
    }
    // Output
    cout << password;
    return 0;
}