#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


string longestCommonPrefix(vector<string> &strs)
{
    string res = "";
    if (strs.size() == 0)
    {
        return "";
    }
    for (auto i = 0; i < strs[0].size(); i++)
    {
        auto tmpchar = strs[0][i];
        for (auto j = 1; j < strs.size(); j++)
        {
            if (strs[j].size() <= i || strs[j][i] != tmpchar)
            {
                return res;
            }
        }
        res.push_back(tmpchar);
    }
    return res;
}

int main()
{
    vector<string> tmp{};
    cout << longestCommonPrefix(tmp) << endl;
    return 0;
}