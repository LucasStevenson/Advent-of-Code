with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines if line.strip()]

left = 0
right = 25
for _ in range(len(lines)):
    preamble = lines[left:right]
    num = lines[right]
    numIsGood = False
    for i in range(len(preamble)-1):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == num:
                # this means that the number is valid and we can stop looping and skip to the next num
                numIsGood = True
                break  # breaks out of the inner loop
        if numIsGood:
            # breaks out of the outer loop
            break
    if numIsGood == False:  # the number is not valid
        print(num)
        break

    # increment the left and right indexes by 1
    left += 1
    right += 1
