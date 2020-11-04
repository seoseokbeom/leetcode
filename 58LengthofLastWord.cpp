#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

vector<string> fun(string line)
{
    vector<string> tokens;
    stringstream check1(line);

    string intermediate;
    while (getline(check1, intermediate, ' '))
    {
        tokens.push_back(intermediate);
    }
    vector<string> res;
    for (int i = 0; i < tokens.size(); i++)
        res.push_back(tokens[i]);
    return res;
}

int lengthOfLastWord(string s)
{
    string chars = 
	for (char c: chars) {
		s.erase(std::remove(s.begin(), s.end(), c), s.end());
	}

    for (auto &v : fun(s))
    {
        cout << v << endl;
    }
    return fun(s).back().size();
}

int main()
{
    cout << lengthOfLastWord("b     a         ");
    return 0;
}