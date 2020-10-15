#include <algorithm>
#include <cctype>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    char c;
    cout << "Enter a char: ";
    cin >> c;
    char upper_case_c = toupper(c);

    cout << "Your uppercase: " << upper_case_c << endl;
}