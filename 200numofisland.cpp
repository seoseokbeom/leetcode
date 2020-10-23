#include <iostream>
#include <vector>
// #include <pair>
#include <queue>
#include <algorithm>
#include <sstream>

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

void dfs(vector<vector<char>> &grid, int i, int j)
{
    if (i < 0 || i > grid.size() || j < 0 || j > grid[0].size() || grid[i][j] == 0)
    {
        return;
    }
    grid[i][j] = 0;
    dfs(grid, i - 1, j);
    dfs(grid, i + 1, j);
    dfs(grid, i, j - 1);
    dfs(grid, i, j + 1);
}

// int numIslands(vector<vector<char>> &grid)
// {
//     int res = 0;
//     // cout << 222 << res << endl;
//     for (int i = 0; i < grid.size(); i++)
//     {
//         for (int j = 0; j < grid[0].size(); j++)
//         {
//             if (grid[i][j] == 1)
//             {
//                 res++;
//                 // cout << res << endl;
//                 dfs(grid, i, j);
//             }
//         }
//     }
//     // cout << res << endl;
//     return res;
// }

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

// int main()
// {
//     vector<vector<char>> tmp2{
//         {1, 1, 1, 1, 0},
//         {1, 1, 0, 1, 0},
//         {1, 1, 0, 0, 0},
//         {0, 0, 0, 0, 0}};
//     // cout << tmp2 << endl;
//     for (int i = 0; i < tmp2.size(); i++)
//     {
//         for (int j = 0; j < tmp2[0].size(); j++)
//         {
//             cout << tmp2[i][j] << ' ';
//         }
//         cout << endl;
//     }
//     int res2 = numIslands(tmp2);
//     cout << res2 << endl;
//     for (int i = 0; i < resarr.size(); i++)
//     {
//         cout << resarr[i] << ' ';
//     }
//     return 0;
// }
