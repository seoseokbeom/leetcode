#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int arrayNesting(vector<int> &nums)
{
    int res = 1;
    for (int i = 0; i < nums.size(); i++)
    {
        auto cnt = 0;
        auto v = i;
        while (nums[v] >= 0)
        {
            cnt++;
            cout << v << endl;
            auto k = nums[v];
            nums[v] = -1;
            v = k;
            res = max(res, cnt);
        }
    }
    return res;
}

int main()
{
    vector<int> tmp{5, 4, 0, 3, 1, 6, 2};
    cout << arrayNesting(tmp) << endl;
    return 0;
}