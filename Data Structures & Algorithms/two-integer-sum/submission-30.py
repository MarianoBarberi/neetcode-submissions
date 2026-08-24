class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = defaultdict(int)

        for i, num in enumerate(nums):
            targetNum = target - num

            if targetNum in hashNums:
                return [hashNums[targetNum], i]
            
            hashNums[num] = i