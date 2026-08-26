class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        nums = sorted(nums)

        l, r = 0, 1
        maxAns = 1
        ans = 1
        while r <= len(nums) - 1:
            if nums[r] != nums[l]:
                if nums[r] - nums[l] == 1:
                    ans += 1
                    maxAns = max(maxAns, ans)
                else:
                    ans = 1
            r += 1
            l += 1
        
        return maxAns