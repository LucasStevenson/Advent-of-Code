with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines if line.strip()]
lines.sort()
lines.insert(0, 0)

d = {}


def numPermutations(index):
    # need to use memoization to shorten runtime
    if index == len(lines) - 1:
        return 1

    if index in d:
        return d[index]
    count = 0
    for i in range(index+1, len(lines)):
        if lines[i] - lines[index] <= 3:
            count += numPermutations(i)
    d[index] = count
    return count


print(numPermutations(0))
