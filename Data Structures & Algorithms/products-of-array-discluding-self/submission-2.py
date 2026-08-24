class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, ans = [], 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans = ans * nums[j]
            res.append(ans)
            ans = 1
        return res