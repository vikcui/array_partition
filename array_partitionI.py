# author: YANG CUI

def arrayPairSum_built_in(nums):
    nums.sort()
    return sum(nums[::2])

def arrayPairSum_own(nums):
    # first sort nums O(nlogn)
    nums.sort()
    sum = 0
    for i in range(len(nums)//2):
        sum += nums[2 * i]
    # print(sum)
    return sum
# arrayPairSum([1,0,3,2])
# A = [1,2,3,4]
# print(A[::2])