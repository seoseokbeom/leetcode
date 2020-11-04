#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;
int cement(int *solid, int width)
{
    int mxL = 0, mxR = 0;
    int l = 0;
    int r = width - 1;
    int cimentAmount = 0;
    while (l <= r)
    {
        if (solid[l] <= solid[r])
        {
            if (solid[l] >= mxL)
                mxL = solid[l];
            else
            {
                cimentAmount += mxL - solid[l];
                solid[l] = mxL;
            }
            l++;
        }
        else
        {
            if (solid[r] >= mxR)
                mxR = solid[r];
            else
            {
                cimentAmount += mxR - solid[r];
                solid[r] = mxR;
            }
            r--;
        }
    }
    return cimentAmount;
}

void solution(int day, int width, int **blocks)
{
    // int initial[]
    int res = 0;

    int *initial = new int[width];
    for (int i = 0; i < width; i++)
    {
        initial[i] = 0;
    }

    for (int i = 0; i < day; i++)
    {
        for (int j = 0; j < width; j++)
        {
            initial[j] += blocks[i][j];
        }
        // for (int i = 0; i < width; i++)
        // {
        //     cout << initial[i] << ' ';
        // }
        // cout << endl;
        //(sizeof(initial) / sizeof(*initial))
        res += cement(initial, width);
        // cout << "after cement" << endl;
        // for (int i = 0; i < width; i++)
        // {
        //     cout << initial[i] << ' ';
        // }
        // cout << endl;
    }
    cout << res << endl;
    return;

    int brick[] = {6, 2, 11, 0, 3, 5};
    // cout << brick.size() << endl;
    cout << cement(brick, (sizeof(brick) / sizeof(*brick))) << endl;
    int secondBrick[] = {6, 3, 0, 9, 0, 5};
    for (int i = 0; i < (sizeof(brick) / sizeof(*brick)); i++)
    {
        // cout << brick[i] << ' ';
        brick[i] += secondBrick[i];
    }
    cout << cement(brick, (sizeof(brick) / sizeof(*brick))) << endl;
}
// //////////////

struct input_data
{
    int day;
    int width;
    int **blocks;
};

void process_stdin(struct input_data &inputData)
{
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.day;

    getline(cin, line);
    iss.clear();
    iss.str(line);
    iss >> inputData.width;

    inputData.blocks = new int *[inputData.day];
    for (int i = 0; i < inputData.day; i++)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.blocks[i] = new int[inputData.width];
        for (int j = 0; j < inputData.width; j++)
        {
            iss >> inputData.blocks[i][j];
        }
    }
}

int main()
{
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.day, inputData.width, inputData.blocks);
    return 0;
}