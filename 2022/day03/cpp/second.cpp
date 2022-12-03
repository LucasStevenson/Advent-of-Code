#include <iostream>
#include <set>
#include <fstream>
#include <algorithm>
#include <cctype>
#include <vector>
using namespace std;

int solution(ifstream& file) {
    string line;
    int ans = 0;
    vector<set<char>> list; 
    while (getline(file, line)) {
        set<char> s(line.begin(), line.end()); // convert line to set  
        if (list.size() < 2) {
            list.push_back(s);
            continue;
        }
        // at this point, `list` has the previous two lines
        // `s` is the third (and the last) line in the current "group" (because a group is 3 lines)
        set<char> first = list[0], second = list[1];
        set<char> intersect1; // this will hold the intersection between `first` and `second`
        set<char> intersection; // this will hold the intersection between all three of the sets
        set_intersection(first.begin(), first.end(), second.begin(), second.end(), inserter(intersect1, intersect1.begin()));
        set_intersection(intersect1.begin(), intersect1.end(), s.begin(), s.end(), inserter(intersection, intersection.begin()));
        ans += islower(*intersection.begin()) ? *intersection.begin()-'a'+1 : *intersection.begin()-'A'+27;
        list.clear();
    }
    return ans;
}

int main(int argc, char** argv)  {
    string infile = argc == 2 ? argv[1] : "input.txt";
    ifstream file(infile);
    cout << solution(file) << endl;
    file.close();
    return 0;
}
