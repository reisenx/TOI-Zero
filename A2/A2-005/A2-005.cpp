#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> xWidth, yWidth;
int W, H, M, N;

int main()
{
    // This makes std::cin and std::cout faster
    ios_base::sync_with_stdio(false); cin.tie(0);
    
    // Input size of a bread
    cin >> W >> H >> M >> N;
    // Input vertical bread slices
    int x1 = 0, x2 = 0;
    for(int i = 0; i < M; i++)
    {
        cin >> x2;
        xWidth.push_back(x2 - x1);
        x1 = x2;
    }
    xWidth.push_back(W - x1);
    // Input horizontal bread slices
    int y1 = 0, y2 = 0;
    for(int i = 0; i < N; i++)
    {
        cin >> y2;
        yWidth.push_back(y2 - y1);
        y1 = y2;
    }
    yWidth.push_back(H - y1);
    
    // Sorting in descending order
    sort(xWidth.begin(), xWidth.end(), greater<int>());
    sort(yWidth.begin(), yWidth.end(), greater<int>());
    
    // Calculate maximum area
    int top1 = xWidth[0] * yWidth[0];
    int top2 = max(xWidth[1] * yWidth[0], xWidth[0] * yWidth[1]);
    // Output
    cout << top1 << ' ' << top2;
    return 0;
}