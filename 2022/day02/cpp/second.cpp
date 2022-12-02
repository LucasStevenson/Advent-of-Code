#include <iostream>
#include <map>
#include <fstream>
#include <algorithm>
using namespace std;

int solution(ifstream& file) {
    string line;
    int score = 0;
    map<char, int> weights = {{'A', 1}, {'B', 2}, {'C', 3}};
    map<char, char> iWin = {
        {'A', 'B'},
        {'B', 'C'},
        {'C', 'A'}};
    map<char, char> iLose;
    // inverted `iWin` map
    for (map<char,char>::iterator i = iWin.begin(); i != iWin.end(); i++) {
        iLose[i->second] = i->first;
    }
    while (getline(file, line)) {
        line.erase(remove(line.begin(), line.end(), ' '), line.end()); // remove spaces
        char oppMove = line[0], outcome = line[1];
        score += (outcome - 'X')*3; // adds the points for whether we lost, drew, won
        if (outcome == 'X') { // i lose
            score += weights[iLose[oppMove]];
        } else if (outcome == 'Z') { // i won
            score += weights[iWin[oppMove]];
        } else { // draw
            score += weights[oppMove];
        }
    }
    return score;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "input.txt";
    ifstream file(infile);
    if (!file.is_open()) {
        cerr << "Error while trying to open '" << infile << "'" << endl;
        return 1;
    }
    cout << solution(file) << endl;
}
