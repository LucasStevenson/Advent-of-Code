#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
using namespace std;

int solution(string line, int n) {
    for (int i = 0; i < line.length()-n; i++) {
        set<char> uniq(line.begin()+i, line.begin()+i+n);
        if (uniq.size() == n) {
            return i+n;
        }
    }
    return 0;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "input.txt";
    ifstream file(infile);
    string line;
    getline(file, line);
    cout << "Part 1: " << solution(line, 4) << endl;
    cout << "Part 2: " << solution(line, 14) << endl;
    file.close();
    return 0;
}
