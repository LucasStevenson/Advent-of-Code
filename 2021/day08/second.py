from collections import Counter, defaultdict
import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def sortEachEl(arr):
    return list(map(lambda el: "".join(sorted(el)), arr.split()))

zero = ["seg0", "seg1", "seg2", "seg4", "seg5", "seg6"]
one = ["seg2", "seg5"]
two = ["seg0", "seg2", "seg3", "seg4", "seg6"]
three = ["seg0", "seg2", "seg3", "seg5", "seg6"]
four = [""]
five = []
six = []
seven = []
eight = []
nine = []

with open(infile) as f:
    line = f.readline().rstrip()
    vals = defaultdict(list)
    while line:
        first, second = line.split(" | ")
        first = sortEachEl(first)
        second = sortEachEl(second)
        for i in first:
            if len(i) == 2:
                vals[1] = list(i)
            elif len(i) == 4:
                vals[4] = list(i)
            elif len(i) == 3:
                vals[7] = list(i)
            elif len(i) == 7:
                vals[8] = list(i)

        line = f.readline().rstrip()
    print(vals)
