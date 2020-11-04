#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<int> sortedSquares(vector<int> &A)
{
    int i = 0, j = A.size() - 1;
    vector<int> res;
    
    while (i <= j)
    {
        if (abs(A[i]) < abs(A[j]))
        {
            res.push_back(A[j] * A[j]);
            j -= 1;
        }
        else
        {
            res.push_back(A[i] * A[i]);
            i += 1;
        }
    }
    reverse(res.begin(), res.end());
    return res;
}

int main()
{

    return 0;
}
