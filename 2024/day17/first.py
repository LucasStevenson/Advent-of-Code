import sys, re
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    R = {}
    registers, program = f.read().strip().split("\n\n")
    program = [int(x) for x in re.findall(r"\d+", program)]
    for r in registers.split("\n"):
        register, val = re.search(r"Register (\w): (.+)", r).groups()
        R[register] = int(val)

def combo(operand):
    if 0 <= operand <= 3: return operand
    if operand == 4: return R['A']
    if operand == 5: return R['B']
    if operand == 6: return R['C']

def exec_program(program):
    out = []
    pc = 0
    while pc < len(program):
        opcode, operand = program[pc], program[pc+1]
        if opcode == 0:
            R['A'] >>= combo(operand)
        elif opcode == 1:
            R['B'] ^= operand
        elif opcode == 2:
            R['B'] = combo(operand)%8
        elif opcode == 3 and R['A'] != 0:
            pc = operand
            continue
        elif opcode == 4:
            R['B'] ^= R['C']
        elif opcode == 5:
            out.append(str(combo(operand)%8))
        elif opcode == 6:
            R['B'] = R['A'] >> combo(operand)
        elif opcode == 7:
            R['C'] = R['A'] >> combo(operand)
        pc += 2
    return ",".join(out)

print(exec_program(program))
