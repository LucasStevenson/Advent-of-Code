'''
https://adventofcode.com/2020/day/4#part2
'''

# NEW/UPDATED SOLUTION

import re
with open("input.txt") as f:
    passports = []
    passport = {}
    readFile = f.read().split("\n")

    for line in readFile:
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            for i in line.split():
                passport[i.split(':')[0]] = i.split(':')[1]

count = 0
for d in passports:
    good = True
    if "byr" not in d or int(d["byr"]) not in range(1920,2003):
        good = False
    if "iyr" not in d or int(d["iyr"]) not in range(2010, 2021):
        good = False
    if "eyr"  not in d or int(d["eyr"]) not in range(2020, 2031):
        good = False
    if "hcl" not in d or not bool(re.match(r"(#[0-9a-f]{6}$)", d["hcl"])):
        good = False
    if "ecl" not in d or not bool(re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", d["ecl"])):
        good = False
    if "pid" not in d or not bool(re.match(r"(\d{9})$", d["pid"])):
        good = False

    if "hgt" not in d or not bool(re.search(r"[cm|in]", d["hgt"])):
        good = False
    else:
        num = int(re.match(r"(\d+)", d["hgt"])[0])
        if "cm" in d["hgt"] and num not in range(150, 194):
            good = False
        elif "in" in d["hgt"] and num not in range(59,77):
            good = False
    if good:
        count += 1
print(count)

'''
# ORIGINAL SOLUTION

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
    keys = {}
    for j in i.split():
        key, val = j.split(":")[0], j.split(":")[1]
        if key != "cid":
            keys[key] = val
    passports.append(keys)


def checkPassport(obj):
    if (len(obj) < 7):
        return False

    # put all the conditions into variables. Split up the conditions into different variables to keep it somewhat neat
    conditions1 = int(obj["byr"]) >= 1920 and int(obj["byr"]) <= 2002 and int(obj["iyr"]) >= 2010 and int(
        obj["iyr"]) <= 2020 and int(obj["eyr"]) >= 2020 and int(obj["eyr"]) <= 2030

    conditions2 = False
    if obj["hgt"][-2:] == "in":
        conditions2 = int(obj["hgt"][:-2]) >= 59 and int(obj["hgt"][:-2]) <= 76
    elif obj["hgt"][-2:] == "cm":
        conditions2 = int(
            obj["hgt"][:-2]) >= 150 and int(obj["hgt"][:-2]) <= 193

    conditions3 = len((obj["pid"])) == 9 and obj["ecl"] in [
        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and obj["hcl"][0] == "#" and len(obj["hcl"]) == 7

    if conditions1 and conditions2 and conditions3:
        for i in obj["hcl"][1:]:
            if i not in ["0", "1", "2", '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return False
        return True
    return False


validCount = 0
for passport in passports:
    if checkPassport(passport):
        validCount += 1
        print(validCount)
'''
