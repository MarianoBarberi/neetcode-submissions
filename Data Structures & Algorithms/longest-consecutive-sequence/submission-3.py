class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        print(nums)
        total_max, local_max = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                local_max += 1
            else:
                local_max = 1
            if local_max > total_max:
                total_max = local_max
        return total_max