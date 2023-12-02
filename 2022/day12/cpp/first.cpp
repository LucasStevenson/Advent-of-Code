#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <deque>
#include <tuple>
using namespace std;

int solution(vector<vector<char>>& grid) {
    int sr, sc, fr, fc; // starting [row,col], final [row,col]
    bool foundStart = false, foundEnd = false;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == 'S') {
                sr = i;
                sc = j;
                grid[i][j] = 'a';
                foundStart = true;
            }
            else if (grid[i][j] == 'E') {
                fr = i;
                fc = j;
                grid[i][j] = 'z';
                foundEnd = true;
            }
        }
        if (foundStart && foundEnd) break;
    }
    // main idea is to use BFS
    // going to have a queue of tuples
    // each tuple holds three values: (rowPos, colPos, numSteps)
    deque<tuple<int, int, int>> Q = {{sr, sc, 0}}; // initialize to (startingRow, startingCol, 0 steps)
    set<tuple<int,int>> visited = {{sr,sc}}; // visited positions
    vector<tuple<int, int>> directions = {{0,1},{0,-1},{1,0},{-1,0}}; 
    while (!Q.empty()) {
        auto& [r, c, numSteps] = Q.back();
        Q.pop_back();
        if (r == fr && c == fc) {
            return numSteps;
        }
        for (auto& [dr, dc] : directions) {
            int rr = r+dr;
            int cc = c+dc;
            if (visited.find({rr,cc}) != visited.end()) {
                // then it exists in visited, skip it
                continue;
            }
            if (!((0 <= rr && rr < grid.size()) && (0 <= cc && cc < grid[r].size()))) {
                continue;
            }
            if (grid[rr][cc] - grid[r][c] > 1) {
                continue;
            }
            Q.push_front({rr,cc,numSteps+1});
            visited.insert({rr,cc});
        }
    }
    return -1;
}

vector<vector<char>> createGrid(ifstream& file) {
    string line;
    vector<vector<char>> grid;
    while (getline(file, line)) {
        vector<char> splitted;
        for (auto& c : line) {
            splitted.push_back(c);
        }
        grid.push_back(splitted);
    }
    return grid;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    vector<vector<char>> grid = createGrid(file);
    cout << solution(grid) << endl;
    file.close();
    return 0;
}
