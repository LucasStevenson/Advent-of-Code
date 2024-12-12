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

def get_chunk_startIdx(arr, idx):
    for i in range(idx-1, -1, -1):
        if arr[i] != arr[idx]:
            return i+1
    return 1

def moveBlocks(arr):
    i, jj = arr.index('.'), len(arr)-1
    while jj > 0:
        while i < jj:
            if arr[i] != '.':
                i += 1
                continue
            if arr[jj] == '.':
                jj -= 1
                continue
            j = get_chunk_startIdx(arr, jj) 
            i_end, j_end = i+jj-j+1, jj+1
            if len(arr[i:i_end]) >= len(arr[j:j_end]) and all(x == '.' for x in arr[i:i_end]):
                # swap the chunks of data
                arr[j:j_end], arr[i:i_end] = arr[i:i_end], arr[j:j_end]
            else:
                i += 1
                continue
            i = arr.index('.')
            jj = j-1
        i = arr.index('.')
        jj = get_chunk_startIdx(arr, jj)-1
    return arr

ordered_blocks = moveBlocks(expanded_data)
def calc_checksum(arr):
    return sum([ i*int(c) for i, c in enumerate(arr) if c != '.' ])
print(calc_checksum(ordered_blocks))
