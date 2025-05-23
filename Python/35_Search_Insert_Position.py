nums = [1,3,5,6]
target = 7



def left_border(nums,target):
    left = -1
    right = len(nums)
    while right - left > 1:
        middle = (left + right)//2
        if nums[middle] < target:
            left = middle
        else:
            right = middle
    return left

def right_border(nums,target):
    left = -1
    right = len(nums)
    while right - left > 1:
        middle = (left + right)//2
        if nums[middle] < target:
            left = middle
        else:
            right = middle
    return right

print(right_border(nums,target), left_border(nums,target) )

