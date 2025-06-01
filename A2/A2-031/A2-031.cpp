#include<iostream>
#include<vector>
using namespace std;

int N, M, cnt = 0;
vector<vector<char>> DNA;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);

    // Input DNA
    cin >> N;
    DNA.assign(2, vector<char>(N));
    for(int i = 0; i < N; i++) { cin >> DNA[0][i]; }
    for(int i = 0; i < N; i++) { cin >> DNA[1][i]; }

    // Changes DNA lines
    cin >> M;
    while(M--)
    {
        int line, pos;
        char gene;
        cin >> line >> pos >> gene;
        DNA[line - 1][pos] = gene;
    }

    // Output new DNA lines
    for(char &gene : DNA[0]) { cout << gene << ' '; }
    cout << '\n';
    for(char &gene : DNA[1]) { cout << gene << ' '; }
    cout << '\n';

    // Count matched gene pair
    for(int i = 0; i < N; i++)
    {
        if(DNA[0][i] == 'A' && DNA[1][i] == 'T') { cnt++; }
        if(DNA[0][i] == 'T' && DNA[1][i] == 'A') { cnt++; }
        if(DNA[0][i] == 'C' && DNA[1][i] == 'G') { cnt++; }
        if(DNA[0][i] == 'G' && DNA[1][i] == 'C') { cnt++; }
    }
    // Output unmatched gene pair
    cout << N - cnt << '\n';
    return 0;
}