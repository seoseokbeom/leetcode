#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

int findDuplicate(vector<int> &nums)
{
    set<int> vis;
    for (int i = 0; i < nums.size(); i++)
    {
        if (vis.find(nums[i]) != vis.end())
        {
            return nums[i];
        }
        vis.insert(nums[i]);
    }
    return -1;
}

int main()
{
    vector<int> tmp{1, 3, 4, 2, 2};
    cout << findDuplicate(tmp) << endl;

    return 0;
}
