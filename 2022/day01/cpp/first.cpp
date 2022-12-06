#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>

int solution(std::ifstream& file) {
    std::string line;
    int ans = INT_MIN;
    int sum = 0;
    while (std::getline(file, line)) {
        if (line == "") {
            // we've reached an empty line
            ans = std::max(ans, sum);
            sum = 0; // reset sum variable
            continue;
        }
        sum += std::stoi(line);
    }
    return std::max(ans, sum);
}

int main(int argc, char** argv) {
    // challenge input parsing
    std::string infile = argc == 2 ? argv[1] : "../input.txt";
    std::ifstream file(infile);
    if (!file.is_open()) {
        std::cerr << "Failed to open '" << infile << "'" << std::endl;
        return 1;
    }
    std::cout << solution(file) << std::endl;
    file.close();
    return 0;
}
