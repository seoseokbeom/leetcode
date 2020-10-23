#include <iostream>
#include <vector>
using namespace std;

int countOdds(int low, int high)
{
    int res = 0;
    for (int i = low + !(low % 2); i <= high - !(high % 2); i += 2)
    {
        res++;
    }
    return res;
}
int main()
{
    cout << countOdds(8, 10) << endl;
    cout << countOdds(3, 7) << endl;
    cout << countOdds(4, 7) << endl;

    return 0;
}