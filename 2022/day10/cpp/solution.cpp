#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;

vector<string> split(string, string);

map<int, int> parseInput(ifstream& file) {
    map<int, int> obj;
    int X = 1;
    int cycle = 0;
    string line;
    while (getline(file, line)) {
        auto splitted = split(line, " ");
        if (splitted.size() == 1) { // noop
            cycle++;
            obj[cycle] = X;
        } else { // addx
            int amt = stoi(splitted[1]);
            cycle++;
            obj[cycle] = X;
            cycle++;
            obj[cycle] = X;
            X += amt;
        }
    }
    return obj;
}

int part1(map<int,int>& obj) {
    int s = 0;
    int nums[] = { 20, 60, 100, 140, 180, 220 };
    for (auto& x : nums) {
        s += x*obj[x];
    }
    return s;
}

void part2(map<int,int>& obj) {
    int pixelPos = 0;
    for (int r = 0; r < 6; r++) {
        for (int c = 0; c < 40; c++) {
            int spritePos = obj[pixelPos+1];
            if (spritePos-1 <= c && c <= spritePos+1) { // c is equivalent to pixelPos%40
                cout << "#" << " ";
            } else {
                cout << " " << " ";
            }
            pixelPos++;
        }
        cout << endl;
    }
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    auto obj = parseInput(file);
    cout << "Part 1: " << part1(obj) << endl;
    cout << "Part 2:" << endl;
    part2(obj);
    file.close();
    return 0;
}

vector<string> split(string s, string delim) {
    size_t pos = 0;
    string token;
    vector<string> V;
    while ((pos = s.find(delim)) != string::npos) {
        token = s.substr(0, pos);
        V.push_back(token);
        s.erase(0, pos+delim.length());
    }
    V.push_back(s);
    return V;
}
