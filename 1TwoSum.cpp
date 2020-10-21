#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> imap;
        for (int i = 0;; ++i)
        {
            auto it = imap.find(target - nums[i]);
            if (it != imap.end())
                return vector<int>{i, it->second};
            imap[nums[i]] = i;
        }
    }
};

int main()
{
    Solution myObj;
    vector<int> tmp{2, 7, 11, 15};
    vector<int> res = myObj.twoSum(tmp, 9);
    for (int x : res)
    {
        cout << x << ' ';
    }
    return 0;
}