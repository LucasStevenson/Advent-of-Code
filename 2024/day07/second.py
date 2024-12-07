import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def isGood(guess, nums):
    if len(nums) == 1:
        return nums[0] == guess
    l1 = [nums[0]*nums[1]] + nums[2:]
    l2 = [nums[0]+nums[1]] + nums[2:]
    l3 = [int(str(nums[0])+str(nums[1]))] + nums[2:]
    return isGood(guess, l1) or isGood(guess, l2) or isGood(guess, l3)

with open(infile) as f:
    ans = 0
    while line := f.readline().strip():
        guess, nums = line.split(": ")
        nums = [int(x) for x in nums.split()]
        guess = int(guess)
        if isGood(guess, nums):
            ans += guess
    print(ans)
