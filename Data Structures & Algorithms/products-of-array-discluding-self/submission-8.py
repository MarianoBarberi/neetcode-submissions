class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            prod = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    prod *= num2
            ans.append(prod)
        return ans