with open("input.txt") as f:
    line = f.readline()

    sx, sy = 0, 0  # ship coords
    wx, wy = 10, 1  # waypoint coords
    while line:
        action, quantity = line[0], int(line[1:])

        if action == "R":
            for _ in range(quantity // 90):
                tempx = wx
                wx = wy
                wy = -1 * tempx
        elif action == "L":
            for _ in range(quantity // 90):
                tempx = wx
                wx = -1 * wy
                wy = tempx

        if action == "F":
            sx += quantity * wx
            sy += quantity * wy

        if action == "N":
            wy += quantity
        elif action == "E":
            wx += quantity
        elif action == "S":
            wy -= quantity
        elif action == "W":
            wx -= quantity

        line = f.readline()
    print(abs(sx) + abs(sy))
