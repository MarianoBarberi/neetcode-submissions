class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            targetNum = target - num
            if targetNum in nums:
                numsIndex = nums.index(targetNum)
                if i != numsIndex:
                    return [min(i, numsIndex), max(i, numsIndex)]