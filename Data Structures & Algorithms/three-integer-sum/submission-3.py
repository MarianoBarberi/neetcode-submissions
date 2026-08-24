class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while i < len(nums) - 2 and l != len(nums) - 1:
                if [nums[i], nums[l], nums[r]] not in res and nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                r -= 1
                if l == r:
                    l += 1
                    r = len(nums) - 1
        
        return res