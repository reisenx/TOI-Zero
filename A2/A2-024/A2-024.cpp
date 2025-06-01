#include<iostream>
#include<vector>
using namespace std;

int L, P, jump[3], pos[3] = {0, 0, 0}, total[3] = {0, 0, 0}, maxTotal = 0;
const string ANIMAL[3] = {"Rabbit ", "Monkey ", "Frog "};
vector<int> points;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input track length and checkpoint
    cin >> L >> P;
    // Input jump distance of rabbit, monkey and frog
    cin >> jump[0] >> jump[1] >> jump[2];
    // Input checkpoints
    points.assign(L + 1, 0);
    while(P--)
    {
        int idx, value;
        cin >> idx >> value;
        points[idx] = value;
    }
    
    // Each animal jump through the track
    for(int i = 0; i < 3; i++)
    {
        // Calculate total points of each animals
        while(pos[i] <= L)
        {
            total[i] += points[pos[i]];
            pos[i] += jump[i];
        }
        // Find maximum score
        maxTotal = max(maxTotal, total[i]);
    }
    
    // Output
    for(int i = 0; i < 3; i++)
    {
        if(total[i] == maxTotal)
        {
            cout << ANIMAL[i] << total[i] << '\n';
        }
    }
    return 0;
}