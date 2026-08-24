class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hmap and i != hmap[complement]:
                return [hmap[complement], i]
            else:
                hmap[num] = i