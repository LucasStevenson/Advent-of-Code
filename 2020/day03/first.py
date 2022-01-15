'''
https://adventofcode.com/2020/day/3
'''

with open("input.txt") as f:
    line = f.readline() 
    gameMap = []
    while line:
        gameMap.append(line.rstrip())
        line = f.readline()
rise = 0
run = 0
# SLOPE = -1/3
counter = 0
for _ in range(len(gameMap)):
    #print([rise%len(gameMap), run%len(gameMap[rise])])
    if (gameMap[rise][run%len(gameMap[rise])] == "#"):
        counter += 1
    rise += 1 # next row
    run += 3 # move to the right 3

print(counter)