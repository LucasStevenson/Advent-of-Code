'''
https://adventofcode.com/2020/day/2
'''
with open("input.txt") as f:
    line = f.readline()
    inputs = {"ranges": [], "char": [], "string": []}
    while line:
        result = line.strip().split(": ")

        # before the colon
        leftSide = result[0].split() # ['x-y char']
        ranges, char = leftSide[0].split("-"), leftSide[1]

        inputs["ranges"].append(ranges)
        inputs["char"].append(char)
        inputs["string"].append(result[1])
        line = f.readline()

def checkValid(r, c, s):
    counter = 0
    for i in s:
        if i == c:
            counter += 1
    if (counter >= int(r[0])) and (counter <= int(r[1])):
        return True
    return False

answer = 0
for i in range(len(inputs["ranges"])):
    if (checkValid(inputs["ranges"][i], inputs["char"][i], inputs["string"][i])):
        answer += 1

print(answer)

