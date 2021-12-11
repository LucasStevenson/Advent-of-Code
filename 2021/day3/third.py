with open("input.txt") as f:
    lines = [ line.rstrip() for line in f.readlines() if line.strip() ]
    transposed = list(zip(*lines))


def getMostCommonBit(arr):
    count = 0
    for i in arr:
        count += int(i)
    # if there is the same amount as zeroes as ones, this will still return 1
    return round(count/len(arr))



def o2(arr):
    lc = lines.copy()
    for i, e in enumerate(arr):
        mcb = getMostCommonBit(e)
        print(mcb)
        for byte in lc:
            if int(byte[i]) != mcb:
                lc.remove(byte)
    print(lc)



print(o2(transposed))
                    
