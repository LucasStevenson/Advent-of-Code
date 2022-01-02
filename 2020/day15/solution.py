#!/usr/bin/env python3

with open("input.txt") as f:
    line = [int(n) for n in f.readline().split(",")]


def memoryGame(startingNums, n):
    nums = {}  # numSpoken: turnNum
    turn = 1
    for i in range(len(startingNums)-1):
        nums[startingNums[i]] = turn
        turn += 1

    while turn < n:
        prevNum = startingNums[turn-1]

        if prevNum not in nums:
            currNum = 0
        else:
            currNum = turn - nums[prevNum]
        nums[prevNum] = turn
        startingNums.append(currNum)
        turn += 1
    return startingNums[-1]


# first part
first = 2020
print(str(first) + "th number is: " + str(memoryGame(line, first)))

# second part
second = 30000000
print(str(second) + "th number is: " + str(memoryGame(line, second)))
