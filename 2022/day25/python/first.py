import sys
infile = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"

charToNum = {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2,
}
numToChar = { v: k for k,v in charToNum.items() }
with open(infile) as f:
    finalSum = 0
    while line := f.readline().rstrip():
        for i,c in enumerate(line[::-1]):
            finalSum += charToNum[c]*pow(5, i)
ans = ""
# convert base10 sum to "SNAFU" format (base 5 shifted over by 2)
while finalSum != 0:
    rem = finalSum % 5
    finalSum //= 5
    if rem < 3:
        ans = str(rem) + ans
        continue
    ans = numToChar[rem-5] + ans
    finalSum += 1
print(ans)
