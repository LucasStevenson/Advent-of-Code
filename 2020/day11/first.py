with open("input.txt") as f:
    line = f.readline().rstrip()
    lineLength = len(line)
    seatsArray = []
    seatsArray.append(['0'] * (lineLength+2))
    while line:
        if line.strip():
            seatsArray.append(['0'] + list(line) + ['0'])
        line = f.readline().rstrip()
    seatsArray.append(['0'] * (lineLength+2))

'''
def printArr(arr):
    for r in range(1, len(arr)-1):
        for c in range(1, len(arr[r])-1):
            print(arr[r][c], end="")
        print()
'''


def countOccupiedSeats(arr):
    count = 0
    for r in range(1, len(arr)-1):
        for c in range(1, len(arr[r])-1):
            if arr[r][c] == "#":
                count += 1
    return count


# we compare to seatsArray and change the values of seatsArrayClone
seatsArrayClone = [row[:] for row in seatsArray]


def updateSeatsArrayClone(r, c):
    numOccupiedAdjSeats = 0
    adjacentPos = [[r-1, c-1], [r-1, c], [r-1, c+1],
                   [r, c-1], [r, c+1], [r+1, c-1], [r+1, c], [r+1, c+1]]
    for x, y in adjacentPos:
        if seatsArray[x][y] == "#":
            numOccupiedAdjSeats += 1

    if seatsArray[r][c] == "L" and numOccupiedAdjSeats == 0:
        seatsArrayClone[r][c] = "#"
    elif seatsArray[r][c] == "#" and numOccupiedAdjSeats >= 4:
        seatsArrayClone[r][c] = "L"


while True:
    for r in range(1, len(seatsArrayClone)-1):
        for c in range(1, len(seatsArrayClone[r])-1):
            if seatsArray[r][c] != ".":
                updateSeatsArrayClone(r, c)
    # after we compare everything, we see if there was a change between the two arrays
    # if there was, we set em equal to one aonther and reloop
    # else, we count the number of occupied seats and that's our answer
    if seatsArray == seatsArrayClone:
        print(countOccupiedSeats(seatsArray))
        break
    else:
        seatsArray = [row[:] for row in seatsArrayClone]
