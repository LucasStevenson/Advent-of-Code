'''
https://adventofcode.com/2020/day/1
'''
with open("input.txt") as f:
    line = f.readline()
    inputs = []
    while line:
        inputs.append(int(line))
        line = f.readline()

answer = 0
for i in range(0, len(inputs)):
    for j in range(i, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            answer = inputs[i] * inputs[j]
            break
print(answer)
