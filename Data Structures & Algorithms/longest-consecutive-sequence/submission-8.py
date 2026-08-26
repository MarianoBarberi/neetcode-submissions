class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        nums = sorted(set(nums))

        l, r, ans, maxAns = 0, 1, 1, 1
        while r <= len(nums) - 1:
            if nums[r] - nums[l] == 1:
                ans += 1
                if ans > maxAns:
                    maxAns = ans
            else:
                ans = 1
            r += 1
            l += 1
        
        return maxAns