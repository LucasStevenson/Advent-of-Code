#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> parseInput(ifstream& file) {
    string line;
    vector<vector<int>> V;
    while (getline(file, line)) {
        vector<int> nums;
        for (int i = 0; i < line.length(); i++) {
            nums.push_back(line[i]-'0');
        }
        V.push_back(nums);
    }
    return V;
}

int getScore(vector<vector<int>>& lines, int r, int c) {
    int left = 0, right = 0, up = 0, down = 0;
    // check right of (r,c)
    vector<int> V(lines[r].begin()+c+1, lines[r].end());
    for (auto& x : V) {
        right += 1;
        if (x >= lines[r][c]) {
            break;
        }
    }
    // check left of (r,c)
    vector<int> V2(lines[r].begin(), lines[r].begin()+c);
    reverse(V2.begin(), V2.end());
    for (auto& x : V2) {
        left += 1;
        if (x >= lines[r][c]) {
            break;
        }
    }
    // check up
    for (int i = r-1; i >= 0; i--) {
        up += 1;
        if (lines[i][c] >= lines[r][c]) {
            break;
        }
    }
    // check down
    for (int i = r+1; i < lines.size(); i++) {
        down += 1;
        if (lines[i][c] >= lines[r][c]) {
            break;
        }
    }
    return left*up*right*down;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    vector<vector<int>> lines = parseInput(file);
    int ans = 0;
    for (int r = 0; r < lines.size(); r++) {
        for (int c = 0; c < lines[r].size(); c++) {
            ans = max(ans, getScore(lines, r, c));
        }
    }
    cout << ans << endl;
    file.close();
    return 0;
}
