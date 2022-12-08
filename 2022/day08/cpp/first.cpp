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
    if (r == 0 || c == 0 || r == lines.size()-1 || c == lines[r].size()-1) {
        return 1;
    }
    // check right of (r,c)
    int max_elem = *max_element(lines[r].begin()+c+1, lines[r].end());
    if (lines[r][c] > max_elem) {
        return 1;
    }
    // check left of (r,c)
    max_elem = *max_element(lines[r].begin(), lines[r].begin()+c);
    if (lines[r][c] > max_elem) {
        return 1;
    }
    // check up
    int upMax = 0;
    for (int i = 0; i < r; i++) {
        upMax = max(upMax, lines[i][c]);
    }
    if (lines[r][c] > upMax) {
        return 1;
    }
    // check down
    int downMax = 0;
    for (int i = r+1; i < lines.size(); i++) {
        downMax = max(downMax, lines[i][c]);
    }
    if (lines[r][c] > downMax) {
        return 1;
    }
    return 0;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    vector<vector<int>> lines = parseInput(file);
    int ans = 0;
    for (int r = 0; r < lines.size(); r++) {
        for (int c = 0; c < lines[r].size(); c++) {
            ans += getScore(lines, r, c);
        }
    }
    cout << ans << endl;
    file.close();
    return 0;
}
