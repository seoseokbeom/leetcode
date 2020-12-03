#include <iostream>

#include <string>
#include <vector>
using namespace std;

int main(void)
{
    int n;
    cin >> n;
    vector<vector<string>> vec(200, vector<string>(0));
    vector<int> dp(200, 0);
    for (int i = 0; i < n; i++)
    {
        int a;
        string b;
        cin >> a >> b;
        vec[a].push_back(b);
        dp[a] = 1;
    }
    for (int i = 2; i < 200; i++)
    {
        if (dp[i] == 1)
        {

            for (int j = 0; j < vec[i].size(); j++)
            {
                cout << i << " " << vec[i][j] << endl;
            }
        }
    }
    return 0;
}