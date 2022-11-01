# NEW SOLUTION 12/2/21
import re

with open("input.txt") as f:
    line = f.readline()
    obj = {}
    while line.strip():
        pBag = re.search(r"(.+) bags contain", line)[1]
        cBags = re.findall(r"\d (.+?) bag", line)
        obj[pBag] = cBags
        line = f.readline()

def numBags(color):
    parents = []
    for k, v in obj.items():
        if color in v:
            parents.append(k)
    if len(parents) == 0:
        return []
    checkedParents = parents.copy()
    for bagCol in parents:
        checkedParents += numBags(bagCol)
    return set(checkedParents)


print(len(numBags("shiny gold")))





# OLD SOLUTION
'''
import json
https://adventofcode.com/2020/day/7

with open("input.txt") as f:
    line = f.readline()
    inputs = {}
    while line:
        if line.split():
            # set the parent bag color as the KEY and the colors it holds (VALUE) as an array
            parentBag = ' '.join(line.split()[:3]).replace("bags", "")
            childrenBags = []
            innerBags = ' '.join(line.split()[4:])
            # we don't care HOW MANY of each bag it can hold, so we filter that out
            for i in innerBags.split(", "):
                # append the filtered result to childrenBags array
                childrenBags.append(' '.join(i.split()[1:-1]))
            inputs[parentBag.strip()] = childrenBags
        line = f.readline()
#print(json.dumps(inputs, indent=2))


def numBags(color):
    containsColor = []  # keeps track of the bags that hold the specified color
    for k, v in inputs.items():
        # check to see if the colors are in the value arrays
        for el in v:
            if color == el:
                # if it is, append it to containsColor array
                containsColor.append(k)
    checkedColors = []
    if len(containsColor) == 0:
        return []
    for color in containsColor:
        checkedColors.append(color)
        checkedColors += numBags(color)
    return set(checkedColors)


print(len(numBags("shiny gold")))
'''
