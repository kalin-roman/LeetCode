nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = []

def incorrect(nums):
    expectedNums = []
    dupli = []

    ind = 0
    next = 1
    expectedNums.append(nums[0])


    while next < len(nums):
        if nums[ind] == nums[next]:
            next += 1
            dupli.append('_')
        else:
            expectedNums.append(nums[next])
            ind = next
            next += 1
    # for i,x in expectedNums:
    #     nums[i] = x
    # for 
    return nums


def incorrect2(nums):
    k = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            k += 1
            nums[k] = nums[i]
    for x in range(k+1,len(nums)):
        nums[x] = '_'
    
    return k+1


def top(nums):
    a = set(nums)
    nums[:] = sorted(a)
    return len(nums)
print(top(nums))

