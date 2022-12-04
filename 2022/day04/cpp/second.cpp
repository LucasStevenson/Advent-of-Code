#include <iostream>
#include <fstream>
#include <tuple>
using namespace std;

tuple<string, string> split(string s, char delim) {
    int delimIndex = s.find(delim); // returns the index `delim` appears on
    string leftOfDelim = s.substr(0, delimIndex); 
    string rightOfDelim = s.substr(delimIndex+1, s.size());
    return {leftOfDelim, rightOfDelim};
}

tuple<int, int> split_to_int(string s, char delim) {
    // exact same as `split` function, except tuple elements are ints instead of strings
    auto [a, b] = split(s, delim);
    return {stoi(a), stoi(b)};
}

int solution(ifstream& file) {
    string line;
    int count = 0;
    while (getline(file, line)) {
        auto [a, b] = split(line, ',');
        auto [first, second] = split_to_int(a, '-');
        auto [third, fourth] = split_to_int(b, '-');
        if ((third <= first && first <= fourth) || (third <= second && second <= fourth) || (first <= third && third <= second)) {
            // the only difference from part1 is the condition of this if statement
            count++;
        }
    }
    return count;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "input.txt";
    ifstream file(infile);
    cout << solution(file) << endl;
    file.close();
    return 0;
}
