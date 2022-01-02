with open("input.txt") as f:
    lines = f.readlines()
    lines = [line for line in lines if line.strip()]

acc = 0
index = 0
visited = []

while index not in visited:
    cmd = lines[index].split(" ")[0]
    arg = int(lines[index].split(" ")[1])
    if cmd == "acc":
        acc += arg
    elif cmd == "jmp":
        visited.append(index)
        index += arg
        continue
    visited.append(index)
    index += 1

print(acc)
