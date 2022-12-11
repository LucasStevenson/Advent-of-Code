import sys
import re
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

with open(infile) as f:
    monkeys = f.read().split("\n\n")

def parseInput(monkeys):
    monkeyInfo = {}
    N = 1 # product of all mods
    for monkeyNum, monkey in enumerate(monkeys):
        startingItems = re.search(r"Starting items: (.*)\n", monkey).group(1).split(", ")
        operation = re.search(r"new = old (.*)\n", monkey).group(1)
        divisBy = re.search(r"divisible by (\d+)\n", monkey).group(1)
        testTrue = re.search(r"true: throw to monkey (\d+)", monkey).group(1)
        testFalse = re.search(r"false: throw to monkey (\d+)", monkey).group(1)
        N *= divisBy
        monkeyInfo[monkeyNum] = {
                "startingItems": startingItems,
                "operation": operation,
                "divisBy": int(divisBy),
                "testTrue": int(testTrue),
                "testFalse": int(testFalse)
        }
    return monkeyInfo, N

def solution(rounds):
    numInspects = defaultdict(int)
    monkeyInfo, N = parseInput(monkeys)
    for _ in range(rounds):
        for monkeyNum in range(len(monkeyInfo)):
            currMonkey = monkeyInfo[monkeyNum]
            for worryLevel in currMonkey['startingItems']:
                numInspects[monkeyNum] += 1
                worryLevel = str(worryLevel)
                tmpOper = currMonkey['operation'].replace("old", worryLevel)
                newWL = int(eval(worryLevel+tmpOper)) # using eval is bad practice, but it makes doing the operation easier
                newWL %= N
                if newWL % currMonkey['divisBy'] == 0:
                    monkeyInfo[currMonkey['testTrue']]['startingItems'].append(newWL)
                else:
                    monkeyInfo[currMonkey['testFalse']]['startingItems'].append(newWL)
            currMonkey['startingItems'] = []
    #print(numInspects.values())
    sortedVals = sorted(numInspects.values())
    return sortedVals[-1]*sortedVals[-2]

print(solution(10000))
