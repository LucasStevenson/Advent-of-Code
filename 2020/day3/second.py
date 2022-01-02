'''
https://adventofcode.com/2020/day/3#part2
'''

with open("input.txt") as f:
    line = f.readline() 
    gameMap = []
    while line:
        gameMap.append(line.rstrip())
        line = f.readline()


slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]] # [rise, run] format
answer = 1

for slope in slopes:
    rise = 0
    run = 0
    counter = 0
    for _ in range(len(gameMap)):
        if rise <= len(gameMap):
            if (gameMap[rise][run%len(gameMap[rise])] == "#"):
                counter += 1
            rise += slope[0]
            run += slope[1]
        else:
            break
    answer *= counter


print(answer)