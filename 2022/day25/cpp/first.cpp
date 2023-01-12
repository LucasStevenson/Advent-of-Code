#include <iostream>
#include <fstream>
#include <cmath>
#include <bits/stdc++.h>
using namespace std;

string solution(int64_t finalSum) {
    cout << finalSum << endl;
    string ans;
    while (finalSum != 0) {
        uint16_t rem = finalSum % 5;
        finalSum /= 5;
        if (rem < 3) {
            ans = to_string(rem) + ans;
            continue;
        }
        if (rem-5 == -1) {
            ans = "-" + ans;
        } else {
            ans = "=" + ans;
        }
        finalSum += 1;
    }
    return ans;
}

int64_t sumLines(ifstream& file) {
    string line;
    int64_t finalSum;
    while (getline(file, line)) {
        reverse(line.begin(), line.end()); 
        for (int i = 0; i < line.length(); i++) {
            if (isdigit(line[i])) {
                finalSum += (line[i]-'0')*pow(5, i);
                continue;
            }
            if (line[i] == '=') {
                finalSum += -2*pow(5,i);
            } else {
                finalSum += -1*pow(5,i);
            }
        }
    }
    return finalSum;
}

int main(int argc, char** argv) {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    cout << solution(sumLines(file)) << endl;
    return 0;
}
