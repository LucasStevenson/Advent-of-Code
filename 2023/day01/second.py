import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    lines = [ line.strip() for line in f.readlines() if line.strip() ]

def solution(lines):
    ans = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
                continue
            for num, word in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(word):
                    digits.append(str(num+1))
                    break
        ans += int(digits[0] + digits[-1])
    return ans

print(solution(lines))
