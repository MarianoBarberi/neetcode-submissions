class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in nums:
                b = nums.index(ans)
                if b != i:
                    if i < b:
                        return [i,b]
                    else:
                        return [b,i]