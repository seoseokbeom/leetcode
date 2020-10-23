#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution
{
public:
    bool canBeEqual(vector<int> &target, vector<int> &arr)
    {
        unordered_map<int, int> dic1;
        unordered_map<int, int> dic2;
        for (auto &a : arr)
        {
            dic1[a]++;
        }
        for (auto b : target)
        {
            dic2[b]++;
        }
        return dic1 == dic2;
    }
};

int main()
{

    Solution a1;
    vector<int> tmp{12, 3, 4, 5};
    for (auto x : tmp)
        cout << x << endl;
    vector<int> a{1, 2, 3, 4};
    vector<int> b{2, 4, 1, 3};
    cout << 'true' if;
}