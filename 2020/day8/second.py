with open("input.txt") as f:
    lines = f.readlines()
    lines = [line for line in lines if line.strip()]


def loop(l):
    acc = 0
    index = 0
    visited = []
    while index not in visited:
        cmd = l[index].split(" ")[0]
        arg = int(l[index].split(" ")[1])
        if cmd == "acc":
            acc += arg
            visited.append(index)
            index += 1
        elif cmd == "jmp":
            visited.append(index)
            index += arg  # we can't use the continue statement like how we did in the previous part or else we skip over the if statement below
        elif cmd == "nop":
            visited.append(index)
            index += 1

        if index >= len(l):  # we know there's no infinite loop if we reach the end
            return acc
    return False  # there was an infinite loop


for i in range(len(lines)):
    # make a copy of the original list to pass as parameter to loop function
    list2 = list(lines)
    if "jmp" in list2[i]:
        list2[i] = list2[i].replace("jmp", "nop")
        res = loop(list2)
        if res != False:
            print(res)
            break
