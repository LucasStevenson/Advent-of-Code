#include <iostream>
#include <map>
#include <fstream>
#include <algorithm>
using namespace std;

int solution(ifstream& file) {
    string line;
    map<string, int> outcomes = {
        {"AX", 3},
        {"AY", 6},
        {"AZ", 0},
        {"BX", 0},
        {"BY", 3},
        {"BZ", 6},
        {"CX", 6},
        {"CY", 0},
        {"CZ", 3}};
    int score = 0;
    while (getline(file, line)) {
        line.erase(remove(line.begin(), line.end(), ' '), line.end());
        score += line[1] - 'X' + 1;
        score += outcomes[line];
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
