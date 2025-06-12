import sys, re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    starts, commands = f.read().split("\n\n")
    D = {} # {wire: binary value}
    for line in starts.split("\n"):
        wire, val = line.split(": ")
        D[wire] = int(val)
    
commands = commands.strip().split("\n")
for command in commands:
    wire1, op, wire2, outputWire = re.search(r"(.+) (AND|XOR|OR) (.+) \-\> (.+)", command).groups()
    if not (wire1 in D and wire2 in D):
        commands.append(command)
        continue
    output = None
    if op == "AND":
        output = D[wire1] & D[wire2]
    elif op == "XOR":
        output = D[wire1] ^ D[wire2]
    elif op == "OR":
        output = D[wire1] | D[wire2]
    D[outputWire] = output

bin_str = ""
for k, v in dict(sorted(D.items(), reverse=True)).items():
    if not k.startswith("z"):
        break
    bin_str += str(v)
print(int(bin_str, 2))
