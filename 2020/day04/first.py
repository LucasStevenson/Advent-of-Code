'''
https://adventofcode.com/2020/day/4
'''
with open("input.txt") as f:
    arr = []
    string = ""
    for line in f:
        if line.strip():  # if there is no blank line
            string += line.rstrip() + " "
        else:
            arr.append(string)
            string = ""
    arr.append(string)

passports = []
for i in arr:
    keys = []
    for j in i.split():
        # we only care about the keys because the values don't matter in this situation
        key = j.split(":")[0]
        if key != "cid":
            keys.append(key)
    passports.append(keys)

validCount = 0
for i in passports:
    if len(i) >= 7:
        validCount += 1

print(validCount)
