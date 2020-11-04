#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <unordered_map>
using namespace std;

string reorganizeString(string S)
{
    unordered_map<char, int> umap;
    for (auto v : S)
    {
        umap[v] += 1;
    }
    for (auto elem : umap)
    {
        cout << elem.first << ' ' << elem.second << endl;
        if (elem.second > S.size() / 2 + 1)
        {
            return "";
        }
        
    }
}

int main()
{
    reorganizeString("aab");
    return 0;
}