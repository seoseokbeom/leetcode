#include <iostream>
#include <vector>
#include <set>
using namespace std;
vector<int> findDisappearedNumbers(vector<int> &nums)
{
    vector<int> dp(nums.size() + 1);
    for (int i = 0; i < nums.size(); i++) {
        dp[nums[i]] = 1;
    }
    vector<int> res;
    for (int i = 1; i < dp.size(); i++) {
        if (dp[i] == 0) {
            res.push_back(i);
        }
    }
    return res;
}

int main()
{
    vector<int> a{2, 4, 5};
    findDisappearedNumbers(a);

    return 0;
}