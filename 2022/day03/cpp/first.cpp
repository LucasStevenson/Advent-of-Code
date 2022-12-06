#include <iostream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cctype>
using namespace std;

int solution(ifstream& file) {
    string line;
    int ans = 0;
    while (getline(file, line)) {
        string fh = line.substr(0, line.length()/2), sh = line.substr(line.length()/2); // get the first and second half of line as strings
        // convert strings to sets
        set<char> firstHalf(fh.begin(), fh.end());
        set<char> secondHalf(sh.begin(), sh.end());
        set<char> intersection; //save the intersection of the two sets
        set_intersection(firstHalf.begin(), firstHalf.end(), secondHalf.begin(), secondHalf.end(), inserter(intersection, intersection.begin()));
        ans += islower(*intersection.begin()) ? *intersection.begin()-'a'+1 : *intersection.begin()-'A'+27;
    }
    return ans;
}

int main(int argc, char** argv)  {
    string infile = argc == 2 ? argv[1] : "../input.txt";
    ifstream file(infile);
    cout << solution(file) << endl;
    file.close();
    return 0;
}
