nums = [0,1,2,2,3,0,4,2]
val = 2
x = 0

# for i in range(len(nums)):
#     if i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#         else:
#             k += 1

# print(k,nums)
# return k
def roma(nums,val):
    x = 0
    while val in nums:
        if nums[x] == val:
            nums.pop(x)
            x -= 1
        x += 1
    print(len(nums))

def rm(A, n):
    while n in A:
        A.remove(n)
    return len(A)

print(rm(nums, 2))