#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <deque>
#include <regex>
using namespace std;

// functions used in debugging and to see what's going on
void showdq(deque<char>); // prints contents of a deque
void printMap(map<int, deque<char>>); // prints contents of a map

map<int, deque<char>> parseInput(ifstream& file) {
    string line;
    map<int, deque<char>> obj;
    while (getline(file, line)) {
        if (line == "") {
            break;
        }
        //cout << line.length() << endl;
        int crateNum = 0;
        for (int i = 0; i < line.length(); i+=4) {
            if (obj.find(crateNum+1) == obj.end()) { // crameNum+1 does not exist in map
                obj[crateNum+1] = {};
            }
            //cout << i << endl;
            string part = line.substr(i, 4); 
            part.erase(remove(part.begin(), part.end(), ' '), part.end()); // remove spaces
            // cout << "line: " << line << endl;
            // cout << "part: " << part << endl;
            if (part != "" && !isdigit(part[0])) {
                obj[crateNum+1].push_front(part[1]);
            }
            crateNum++;
        }
    }
    return obj;
}

void solution(ifstream& file) {
    string line;
    map<int, deque<char>> obj = parseInput(file);
    // printMap(obj);
    while (getline(file, line)) {
        // cout << line << endl;
        regex pattern(R"(move (\d+) from (\d+) to (\d+))");
        smatch match;
        regex_match(line, match, pattern);
        int amount = stoi(match[1]), fromCrate = stoi(match[2]), toCrate = stoi(match[3]);
        // cout << amount << " " << fromCrate << " " << toCrate << endl;
        for (int i = 0; i < amount; i++) {
            obj[toCrate].push_back(obj[fromCrate].back());
            obj[fromCrate].pop_back();
        }
        // printMap(obj);
    }

    //printMap(obj);
    for (auto& [key, value] : obj) {
        cout << value.back();
    }
    cout << endl;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "input.txt";
    ifstream file(infile);
    solution(file);
    file.close();
    return 0;
}


void showdq(deque<char> d) {
    deque<char>::iterator it;
    for (it = d.begin(); it != d.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

void printMap(map<int, deque<char>> m) {
    for (auto& [key, value] : m) {
        cout << key << ": ";
        showdq(value);
    }
}

