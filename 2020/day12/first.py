with open("input.txt") as f:
    line = f.readline()

    x, y = 0, 0
    degreeFacing = 0  # facing 0 degrees to begin with (east)

    degreeConversion = {
        0: "E",
        90: "N",
        180: "W",
        270: "S"
    }
    while line:
        action, quantity = line[0], int(line[1:])

        if action == "L":
            degreeFacing += quantity
            degreeFacing %= 360
        elif action == "R":
            degreeFacing += 360 - quantity
            degreeFacing %= 360

        if action == "F":
            # check the degreeConversion table
            action = degreeConversion.get(degreeFacing)

        if action == "N":
            y += quantity
        elif action == "E":
            x += quantity
        elif action == "S":
            y -= quantity
        elif action == "W":
            x -= quantity

        line = f.readline()
    print(abs(x) + abs(y))
