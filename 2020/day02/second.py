'''
https://adventofcode.com/2020/day/2#part2
'''
with open("input.txt") as f:
    line = f.readline()
    inputs = {"ranges": [], "char": [], "string": []}
    while line:
        result = line.strip().split(": ")

        # before the colon
        leftSide = result[0].split() # ['x-y char']
        
        ranges, char = leftSide[0].split("-"), leftSide[1]

        inputs["ranges"].append([int(ranges[0])-1, int(ranges[1])-1])
        inputs["char"].append(char)
        inputs["string"].append(result[1])
        line = f.readline()

def checkValid(indexes, char, string):
    counter = 0
    if (string[indexes[0]] == char) ^ (string[indexes[1]] == char):
        return True
    return False

answer = 0
for i in range(len(inputs["ranges"])):
    if (checkValid(inputs["ranges"][i], inputs["char"][i], inputs["string"][i])):
        answer += 1

print(answer)