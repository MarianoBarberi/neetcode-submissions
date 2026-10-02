class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        countingSum = -999999999999999999999999999999999999999
        res = countingSum
        for num in nums:
            if countingSum < 0 and num > countingSum:
                countingSum = num
            else:
                if num < 0:
                    res = max(res,countingSum)
                countingSum += num

        return max(res,countingSum)