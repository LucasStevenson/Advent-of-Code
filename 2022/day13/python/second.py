import sys
import json
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"
with open(infile) as f:
    lines = [ json.loads(line.rstrip()) for line in f.readlines() if line.strip() ]

def compare(left, right):
    # if left and right are both integers, return 1 if left<right, return 0 if left>right, otherwise return nothing 
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left > right:
            return 0
        return 
    # if exactly one of the params is an int, convert the int-param into a list
    if (type(left) == int) ^ (type(right) == int):
        if type(left) == int:
            left = [left]
        else:
            right = [right]
    # if both params are a list, recursively compare their elements
    if type(left) == list and type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            res = compare(left[i], right[i])
            if res == 1:
                return 1
            if res == 0:
                return 0
            i += 1
        # check if right list ran out of items first
        if len(right) < len(left):
            return 0
        if len(right) > len(left):
            return 1
        return

# insert divider packets into input
lines.append([[2]])
lines.append([[6]])

# bubble sort is definitely the easier and more practical way to go about sorting for this challenge
# but I was just recently reading up on quicksort, so I decided to implement it just for the hell of it
def quicksort(arr, start, end):
    if start >= end:
        return
    pivot = partition(arr, start, end)
    quicksort(arr, start, pivot-1)
    quicksort(arr, pivot+1, end)

def partition(arr, start, end):
    wall = start
    for i in range(start, end):
        if compare(arr[i], arr[end]) == 1: 
            arr[i], arr[wall] = arr[wall], arr[i]
            wall += 1
    arr[end], arr[wall] = arr[wall], arr[end]
    return wall

quicksort(lines, 0, len(lines)-1)
print((lines.index([[6]])+1) * (lines.index([[2]])+1))

'''
# bubble sort implementation
for i in range(len(lines)):
    for j in range(0, len(lines)-i-1):
        l, r = lines[j], lines[j+1]
        if compare(l, r) != 1: # if the left is larger than the right
            lines[j],lines[j+1] = lines[j+1], lines[j] # then swap the values
print((lines.index([[6]])+1) * (lines.index([[2]])+1))
'''
