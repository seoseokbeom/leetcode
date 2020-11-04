#include <iostream>
#include <vector>
#include <queue>
#include <sstream>
#include <string>

using namespace std;

string recursion(string numOfOrder, int &i)
{
    string str = "";
    string insideBracket;
    if (i >= numOfOrder.size())
        return str;
    while (i < numOfOrder.size())
    {
        if (numOfOrder[i] == ')')
            return str;
        else if (numOfOrder[i] == 'R' || numOfOrder[i] == 'G' || numOfOrder[i] == 'B')
        {
            if (numOfOrder[i + 1] == '(')
            {
                char save = numOfOrder[i];
                i++;
                insideBracket = recursion(numOfOrder, ++i);
                string tmp = "";
                for (int j = 0; j < insideBracket.size(); j++)
                {
                    tmp += save;
                    tmp += insideBracket[j];
                }
                str += tmp;
            }
            else
            {
                str += numOfOrder[i];
            }
        }
        else if (isdigit(numOfOrder[i]))
        {
            int cnt2 = 0;
            while (isdigit(numOfOrder[i]))
                cnt2 = numOfOrder[i++] + cnt2 * 10 - '0';
            if (numOfOrder[i] == '(')
            {
                insideBracket = recursion(numOfOrder, ++i);
            }
            else
            {
                insideBracket = numOfOrder[i];
            }
            for (int j = 0; j < cnt2; ++j)
                str += insideBracket;
        }
        ++i;
    }
    return str;
}
// string dfs(string s, int i)
// {
//     string res = "";
//     cout << s << endl;
//     if (i >= s.size())
//         return res;
//     while (i < s.size())
//     {
//         if (isalpha(s[i]))
//             res += s[i];
//         else if (s[i] == ')')
//             return res;
//         else if ('0' <= s[i] && s[i] <= '9')
//         {
//             int cnt = 0;
//             while ('0' <= s[i] && s[i] <= '9')
//             {
//                 cnt = cnt * 10 + s[i] - '0';
//                 i++;
//             }
//             string pat = dfs(s, ++i);
//             for (int j = 0; j < cnt; j++)
//             {
//                 res += pat;
//             }
//         }
//         // else
//         //     res += s[i];
//         i++;
//     }
//     return res;
// }

void solution(int numOfOrder, string *orderArr)
{
    // cout << "len: " << sizeof(orderArr) << ' ' << sizeof(*orderArr) << endl;
    // cout << *(orderArr + 1) << endl;
    // string tmp = *(orderArr);
    // cout << typeid(*(orderArr)).name() << endl;
    // cout << *(orderArr) << endl;
    // int cnt = 0;
    // cout << dfs(*(orderArr), cnt) << endl;
    for (int i = 0; i < numOfOrder; i++)
    {
        int cnt = 0;
        cout << recursion(*(orderArr + i), cnt) << endl;
    }
    // (sizeof(brick) / sizeof(*brick))
}

struct input_data
{
    int numOfOrder;
    string *orderArr;
};

void process_stdin(struct input_data &inputData)
{
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.numOfOrder;

    inputData.orderArr = new string[inputData.numOfOrder];
    for (int i = 0; i < inputData.numOfOrder; i++)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        iss >> inputData.orderArr[i];
    }
}

int main()
{
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.numOfOrder, inputData.orderArr);
    return 0;
}