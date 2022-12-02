#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

int solution(std::ifstream& file) {
    std::string line;
    std::vector<int> sums;
    int sum = 0;
    while (std::getline(file, line)) {
        if (line == "") {
            sums.push_back(sum);
            sum = 0;
            continue;
        }
        sum += std::stoi(line);
    }
    if (sum != 0) {
        // this is for the corner case where the last line of input file is NOT empty
        // if that's the case, the sum of the last block will be computed, but not saved to sums vector
        // if `sum` variable is not zero, manually add it to `sums` vector 
	    sums.push_back(sum); 
    }
    std::sort(sums.begin(), sums.end(), std::greater<int>()); // descending order 
    return sums[0]+sums[1]+sums[2];
}

int main(int argc, char** argv) {
    // challenge input parsing
    std::string infile = argc == 2 ? argv[1] : "input.txt";
    std::ifstream file(infile);
    if (!file.is_open()) {
        std::cerr << "Failed to open '" << infile << "'" << std::endl;
        return 1;
    }
    std::cout << solution(file) << std::endl;
    file.close();
    return 0;
}
