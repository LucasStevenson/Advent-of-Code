import sys, re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    actions = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", f.read())
    enabled = True
    ans = 0
    for action in actions:
        if action == 'do()':
            enabled = True
        elif action == "don't()":
            enabled = False
        else:
            if enabled:
                x = re.search(r"mul\((\d+),(\d+)\)", action).groups()
                ans += int(x[0]) * int(x[1])
    print(ans)
