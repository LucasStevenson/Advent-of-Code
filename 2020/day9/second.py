with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines if line.strip()]


def returnBadNum():
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
            return num

        # increment the left and right indexes by 1
        left += 1
        right += 1


badNum = returnBadNum()


def subArraySum(arr, num):
    # https://www.geeksforgeeks.org/find-subarray-with-given-sum/
    n = len(arr)
    curr_sum = arr[0]
    start = 0

    i = 1
    while i <= n:
        while curr_sum > num and start < i-1:

            curr_sum -= arr[start]
            start += 1

        if curr_sum == num:
            ans = lines[start:i-1]
            ans.sort()
            return ans[0] + ans[-1]

        if i < n:
            curr_sum += arr[i]
        i += 1
    return 0


print(subArraySum(lines, badNum))
