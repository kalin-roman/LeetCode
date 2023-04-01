nums = [0,1,1,1,2,2,3,3,4] 
expectedNums = []

ind = 0
next = 1
expectedNums.append(nums[0])


while len(expectedNums) != len(nums):
    nums_equal_expect = nums[ind] == nums[next]
    if nums_equal_expect:
        next += 1
    elif not nums_equal_expect:
        expectedNums.append(nums[next])
        ind = next
    else:
        expectedNums.append('_')

print(expectedNums)