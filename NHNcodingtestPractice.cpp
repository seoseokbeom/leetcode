#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

vector<int> resarr;
int numIslands(vector<vector<int>> &grid)
{
    int m = grid.size(), n = m ? grid[0].size() : 0, area = 0, offsets[] = {0, 1, 0, -1, 0};
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int cnt = 0;
            if (grid[i][j] == 1)
            {
                cnt++;
                queue<pair<int, int>> node;
                area++;
                grid[i][j] = 0;
                node.push({i, j});
                while (!node.empty())
                {
                    pair<int, int> p = node.front();
                    node.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int r = p.first + offsets[k], c = p.second + offsets[k + 1];
                        if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == 1)
                        {
                            cnt++;
                            grid[r][c] = 0;
                            node.push({r, c});
                        }
                    }
                }
                resarr.push_back(cnt);
            }
        }
    }
    return area;
}

void solution(int sizeOfMatrix, int **matrix)
{
    vector<vector<int>> arr;
    for (int i = 0; i < sizeOfMatrix; i++)
    {
        vector<int> miniarr;
        for (int j = 0; j < sizeOfMatrix; j++)
        {
            miniarr.push_back(matrix[i][j]);
        }
        arr.push_back(miniarr);
    }
    int res = numIslands(arr);
    cout << res << endl;
    sort(resarr.begin(), resarr.end());

    for (int i = 0; i < resarr.size(); i++)
    {
        cout << resarr[i] << ' ';
    }
    cout << endl;
}

struct input_data
{
    int sizeOfMatrix;
    int **matrix;
};

void process_stdin(struct input_data &inputData)
{
    string line;
    istringstream iss;

    getline(cin, line);
    iss.str(line);
    iss >> inputData.sizeOfMatrix;

    inputData.matrix = new int *[inputData.sizeOfMatrix];
    for (int i = 0; i < inputData.sizeOfMatrix; i++)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);
        inputData.matrix[i] = new int[inputData.sizeOfMatrix];
        for (int j = 0; j < inputData.sizeOfMatrix; j++)
        {
            iss >> inputData.matrix[i][j];
        }
    }
}

int main()
{
    struct input_data inputData;
    process_stdin(inputData);

    solution(inputData.sizeOfMatrix, inputData.matrix);
    return 0;
}