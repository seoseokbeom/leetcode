#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

using namespace std;

void solution(int sizeOfMatrix, int **matrix)
{
    // TODO: 이곳에 코드를 작성하세요.
}

void dfs(vector<vector<int>> arr, int i, int j)
{

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