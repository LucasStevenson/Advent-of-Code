import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(infile) as f:
    data = list(map(int, f.readline().strip()))
    expanded_data = []
    file_id = 0
    for i, num in enumerate(data):
        if i % 2 == 0:
            expanded_data += [ file_id for _ in range(num) ]
            file_id += 1
        else:
            expanded_data += [ '.' for _ in range(num) ]

def moveBlocks(arr):
    l, r = 0, len(arr)-1
    while l < r:
        if arr[l] != '.':
            l += 1
            continue
        if arr[r] == '.':
            r -= 1
            continue
        arr[l] = arr[r]
        arr[r] = '.'
        l += 1
        r -= 1
    return arr

ordered_blocks = moveBlocks(expanded_data)
def calc_checksum(arr):
    return sum([ i*int(c) for i, c in enumerate(arr[0:arr.index('.')]) ])
print(calc_checksum(ordered_blocks))
