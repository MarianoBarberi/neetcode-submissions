class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        multiplied = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                multiplied *= num
            else:
                zeroCount += 1
        
        if zeroCount > 1:
            return [0] * len(nums)

        for num in nums:
            if zeroCount == 1:
                if num == 0:
                    ans.append(multiplied)
                else:
                    ans.append(0)
            else:
                ans.append(multiplied // num)
        return ans