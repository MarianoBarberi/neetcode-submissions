class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        stringDict = defaultdict(str)
        res = 0
        while r < len(s):
            if s[r] not in stringDict:
                stringDict[s[r]] = 1
                res = max(res,r - l + 1)
                r += 1
            else:
                stringDict.pop(s[l])
                l += 1
                
        return res