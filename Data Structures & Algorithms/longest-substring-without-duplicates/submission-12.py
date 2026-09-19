class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        stringStack = []
        stringDict = defaultdict(str)
        res = 0
        while r < len(s):
            if s[r] not in stringDict:
                stringStack.append(s[r])
                stringDict[s[r]] = 1
                res = max(res,len(stringStack))
                r += 1
            else:
                stringDict.pop(stringStack[0])
                stringStack.pop(0)
                l += 1
                
        return max(res,len(stringStack))