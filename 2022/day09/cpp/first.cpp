#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <tuple>
using namespace std;

bool isTouching(int hx, int hy, int tx, int ty) {
    return (abs(hx-tx) <= 1 && abs(hy-ty) <= 1);
}

int solution(ifstream& file) {
    map<char, tuple<int, int>> obj = {
        {'R', {1,0}},
        {'L', {-1,0}},
        {'U', {0,1}},
        {'D', {0,-1}}
    };
    set<tuple<int,int>> visited;
    int hx=0, hy=0, tx=0, ty=0;
    string line;
    while (getline(file, line)) {
        char dir = line[0];
        auto& [dx, dy] = obj[dir];
        int amt = stoi(line.substr(2,line.length()));
        for (int i = 0; i < amt; i++) {
            visited.insert({tx, ty});
            hx += dx;
            hy += dy;
            if (isTouching(hx, hy, tx, ty)) {
                continue;
            }
            ty += hy==ty ? 0 : (hy-ty)/(abs(hy-ty));
            tx += hx==tx ? 0 : (hx-tx)/(abs(hx-tx));
        }
    }
    return visited.size();
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    cout << solution(file) << endl;
    file.close();
    return 0;
}
