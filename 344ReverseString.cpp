#include <string>
#include <vector>
#include <iostream>

using namespace std;
void reverseString(vector<char> &s)
{
    int i = 0, j = s.size() - 1;
    while (i < j)
    {
        swap(s[i++], s[j--]);
    }
}

int main()
{
    cout << "Hello World"; // prints Hello World
    return 0;
}