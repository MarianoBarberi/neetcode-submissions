class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, ans = [], 1
        for i in range(len(nums)):
            pre = nums[0:i]
            post = nums[i+1:len(nums)]
            for j in range(len(pre)):
                ans = ans * pre[j]
            for k in range(len(post)):
                ans = ans * post[k]
            res.append(ans)
            ans = 1
        return res