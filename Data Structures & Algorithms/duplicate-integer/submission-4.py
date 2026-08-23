class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = {}
        for num in nums:
            if numHash.get(num) == True:
                return True
            numHash[num] = True
        return False