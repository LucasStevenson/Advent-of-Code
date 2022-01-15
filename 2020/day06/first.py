'''
https://adventofcode.com/2020/day/6
'''
with open("input.txt") as f:
    line = f.readline()
    string = ""
    arr = []
    while line:
        if line.strip():  # if the line is not blank
            string += line.rstrip()  # keep on appending the inputs
        else:  # empty line
            arr.append(string)
            string = ""
        line = f.readline()
    arr.append(string)

count = 0
for i in arr:
    filteredInput = set()  # we don't want duplicate values
    for c in i:
        filteredInput.add(c)
    count += len(filteredInput)
print(count)
